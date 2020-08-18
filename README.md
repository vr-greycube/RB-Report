## ReportBro Report

Report Designer using ReportBro for Pdf, Excel reports

Reports using the amazing [ReportBro](https://www.reportbro.com/home/index)

#### Documentation

Complete docs on ReportBro options can be found here [https://www.reportbro.com/docs/userguide](https://www.reportbro.com/docs/userguide)

#### Usage

- Get app and install in your site
- Create a new **RB Report** doc
- To pass dynamic context data set the context_path property to a py controller method, that should return a dictionary of parameters used in the report definition
- Can preview pdf out put by setting parameter values
- To use actually in code:

```
    context = get_context() # some method that returns dictionary with context data
    rb_report = frappe.get_doc("RB Report", report_name)
    pdf = rb_report.get_pdf()
```

#### License

MIT
