# -*- coding: utf-8 -*-
# Copyright (c) 2020, greycube.in and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import cint
from six import string_types, iteritems
from reportbro import *
import json
import io
from reportbro import *


class RBReport(Document):
    def get_definition(self):
        return {
            "docElements": json.loads(self.doc_elements or "[]"),
            "parameters": json.loads(self.parameters or "[]"),
            "styles": json.loads(self.styles or "[]"),
            "documentProperties": json.loads(self.document_properties or "[]"),
            "version": self.version
        }

    def get_pdf(self, context=None, as_download=False, **params):

        if not context and self.context_path:
            context = getattr(frappe.get_module(
                self.context_path), "get_context")(**params)

        if not context:
            context = dict()

        additional_fonts = []
        additional_fonts = [dict(
            value='Arial Unicode MS', filename='/usr/share/fonts/truetype/msttcorefonts/Arial_Unicode_MS.ttf')]

        report_definition = self.get_definition()
        report = Report(report_definition, data=context,
                        additional_fonts=additional_fonts)

        if report.errors:
            # report definition should never contain any errors,
            # unless you saved an invalid report and didn't test in ReportBro Designer
            raise ReportBroError(report.errors[0])

        pdf = report.generate_pdf()
        file_name = context.get(
            "file_name") or "%s.pdf" % frappe.utils.now_datetime()

        if cint(as_download):
            frappe.response.filename = file_name
            frappe.response.filecontent = io.BytesIO(pdf).getvalue()
            frappe.response.type = "download"

        return report.generate_pdf(),


@frappe.whitelist()
def get_pdf(report_name, **args):
    context = args.get("context") or dict()
    if isinstance(context, string_types):
        context = json.loads(context)

    if args.get("context"):
        args.pop("context")

    doc = frappe.get_doc("RB Report", report_name)
    doc.get_pdf(context=context, as_download=True, **args)
