# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "rb_report"
app_title = "ReportBro Report"
app_publisher = "greycube.in"
app_description = "Report Designer using ReportBro for Pdf, Excel reports"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@greycube.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/rb_report/css/rb_report.css"
# app_include_js = "/assets/rb_report/js/rb_report.js"

app_include_css = ["/assets/rb_report/css/reportbro.css",
                   "/assets/rb_report/css/spectrum.min.css"]
app_include_js = [
    "/assets/rb_report/js/reportbro.min.js",
    "/assets/rb_report/js/spectrum.min.js",
    "/assets/rb_report/js/autosize.min.js",
    "/assets/rb_report/js/JsBarcode.all.min.js"
]


# include js, css files in header of web template
# web_include_css = "/assets/rb_report/css/rb_report.css"
# web_include_js = "/assets/rb_report/js/rb_report.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "rb_report.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "rb_report.install.before_install"
# after_install = "rb_report.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "rb_report.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"rb_report.tasks.all"
# 	],
# 	"daily": [
# 		"rb_report.tasks.daily"
# 	],
# 	"hourly": [
# 		"rb_report.tasks.hourly"
# 	],
# 	"weekly": [
# 		"rb_report.tasks.weekly"
# 	]
# 	"monthly": [
# 		"rb_report.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "rb_report.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "rb_report.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "rb_report.task.get_dashboard_data"
# }
