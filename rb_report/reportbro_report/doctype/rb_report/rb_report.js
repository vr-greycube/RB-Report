// Copyright (c) 2020, greycube.in and contributors
// For license information, please see license.txt
const GET_PDF =
  "/api/method/rb_report.reportbro_report.doctype.rb_report.rb_report.get_pdf";
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
      additionalFonts: [
        // { name: "Noto Sans CJK SC Regular", value: "Noto Sans CJK SC Regular" },
      ],
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

    // buttons

    frm.page.add_inner_button("Download Def", () => {
      let rb_def = $("#rb-report").reportBro("getReport");
      downloadify(JSON.stringify(rb_def), `${frm.doc.name}.json`);
    });

    frm.page.add_inner_button("Preview Test", function () {
      let args = {
        context: frappe.rbr.getTestData(),
        report_name: frm.doc.name,
      };
      open_url_post(GET_PDF, args, true);
    });

    frm.page.add_inner_button("Preview", function () {
      let args = frappe.rbr.getTestData()["report_parameters"] || {};
      args["report_name"] = frm.doc.name;
      open_url_post(GET_PDF, args, true);
    });
  },

  validate: function (frm) {
    let rb_def = $("#rb-report").reportBro("getReport");
    console.log(rb_def);
    cur_frm.set_value("definition", JSON.stringify(rb_def));
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

let downloadify = function (data, file_name) {
  var a = document.createElement("a");
  if ("download" in a) {
    // Used Blob object, because it can handle large files
    var blob_object = new Blob([data], { type: "text/json;charset=UTF-8" });
    a.href = URL.createObjectURL(blob_object);
    a.download = file_name;
  } else {
    // use old method
    a.href = "data:application/json," + encodeURIComponent(data);
    a.download = file_name;
    a.target = "_blank";
  }

  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
};
