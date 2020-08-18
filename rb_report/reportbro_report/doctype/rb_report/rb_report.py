# -*- coding: utf-8 -*-
# Copyright (c) 2020, greycube.in and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from reportbro import *
import json
import io


class RBReport(Document):
    def get_definition(self):
        return {
            "docElements": json.loads(self.doc_elements or "[]"),
            "parameters": json.loads(self.parameters or "[]"),
            "styles": json.loads(self.styles or "[]"),
            "documentProperties": json.loads(self.document_properties or "[]"),
            "version": self.version
        }

    def get_pdf(self, **params):
        context = params.get("context") or dict()

        print(params)
        print(type(context), context)

        if not context and self.context_path:
            context = frappe.get_module(self.context_path)(**params)

        report_definition = self.get_definition()
        report = Report(report_definition, data=context)

        if report.errors:
            # report definition should never contain any errors,
            # unless you saved an invalid report and didn't test in ReportBro Designer
            raise ReportBroError(report.errors[0])

        return report.generate_pdf(), context.get("file_name") or "%s.pdf" % frappe.utils.now_datetime()


@frappe.whitelist()
def get_pdf_preview(report_name, data=None):

    if data:
        data = json.loads(data)

    doc = frappe.get_doc("RB Report", report_name)
    pdf_report, file_name = doc.get_pdf(**dict(context=data))

    frappe.response.filename = file_name
    frappe.response.filecontent = io.BytesIO(pdf_report).getvalue()
    frappe.response.type = "download"
