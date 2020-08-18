// Copyright (c) 2020, greycube.in and contributors
// For license information, please see license.txt

frappe.ui.form.on("RB Report", {
  onload: function (frm) {
    // $(document.body).toggleClass("full-width", true);
    frm.page.wrapper.find(".container.page-body").addClass("col-md-12");
    $(frm.fields_dict["rb_html"].wrapper)
      .empty()
      .append(
        $('<div id="rb-report" style="width:800px;height:600px;"></div>')
      );

    frappe.rbr = $("#rb-report").reportBro({
      saveCallback: frm.events.validate,
      //   preview: frm.events.preview_report,
    });

    frm.page.set_secondary_action("Preview Pdf", function () {
      let args = { data: frappe.rbr.getTestData(), report_name: frm.doc.name };
      open_url_post(
        "/api/method/rb_report.reportbro_report.doctype.rb_report.rb_report.get_pdf_preview",
        args,
        true
      );
    });
  },

  refresh: function (frm) {
    if (!frm.is_new()) {
      let report_def = {
        docProperties: JSON.parse(frm.doc.document_properties),
        docElements: JSON.parse(frm.doc.doc_elements),
        parameters: JSON.parse(frm.doc.parameters),
        styles: JSON.parse(frm.doc.styles),
        version: JSON.parse(frm.doc.version),
      };
      frappe.rbr.load(report_def);
    }
  },

  validate: function (frm) {
    let rb_def = $("#rb-report").reportBro("getReport");
    cur_frm.set_value(
      "document_properties",
      JSON.stringify(rb_def.documentProperties)
    );
    cur_frm.set_value("doc_elements", JSON.stringify(rb_def.docElements));
    cur_frm.set_value("parameters", JSON.stringify(rb_def.parameters));
    cur_frm.set_value("styles", JSON.stringify(rb_def.styles));
    cur_frm.set_value("version", JSON.stringify(rb_def.version));
    cur_frm.refresh_fields();
  },

  preview_report: function (frm) {},
});
