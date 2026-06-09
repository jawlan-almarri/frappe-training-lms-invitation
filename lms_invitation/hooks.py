app_name = "lms_invitation"
app_title = "LMS Invitation"
app_publisher = "Jawlan"
app_description = "LMS Invitation Management"
app_email = "Jawlan.almarri@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "lms_invitation",
# 		"logo": "/assets/lms_invitation/logo.png",
# 		"title": "LMS Invitation",
# 		"route": "/lms_invitation",
# 		"has_permission": "lms_invitation.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/lms_invitation/css/lms_invitation.css"
# app_include_js = "/assets/lms_invitation/js/lms_invitation.js"

# include js, css files in header of web template
# web_include_css = "/assets/lms_invitation/css/lms_invitation.css"
# web_include_js = "/assets/lms_invitation/js/lms_invitation.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "lms_invitation/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "lms_invitation/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "lms_invitation.utils.jinja_methods",
# 	"filters": "lms_invitation.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "lms_invitation.install.before_install"
# after_install = "lms_invitation.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "lms_invitation.uninstall.before_uninstall"
# after_uninstall = "lms_invitation.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "lms_invitation.utils.before_app_install"
# after_app_install = "lms_invitation.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "lms_invitation.utils.before_app_uninstall"
# after_app_uninstall = "lms_invitation.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "lms_invitation.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "lms_invitation.notifications.get_notification_config"

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
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"lms_invitation.tasks.all"
# 	],
# 	"daily": [
# 		"lms_invitation.tasks.daily"
# 	],
# 	"hourly": [
# 		"lms_invitation.tasks.hourly"
# 	],
# 	"weekly": [
# 		"lms_invitation.tasks.weekly"
# 	],
# 	"monthly": [
# 		"lms_invitation.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "lms_invitation.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "lms_invitation.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "lms_invitation.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "lms_invitation.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["lms_invitation.utils.before_request"]
# after_request = ["lms_invitation.utils.after_request"]

# Job Events
# ----------
# before_job = ["lms_invitation.utils.before_job"]
# after_job = ["lms_invitation.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"lms_invitation.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []


fixtures = [
    {
        "dt": "Custom Field",
        "filters": [
            ["dt", "=", "Student Enrollment"],
            ["fieldname", "=", "invitation_code"],
        ],
    },
]


doc_events = {
    "Student Enrollment": {
        "validate": "lms_invitation.events.validate_student_enrollment",
        "after_insert": "lms_invitation.events.mark_invitation_code_as_used",
    }
}


scheduler_events = {
    "daily": [
        "lms_invitation.tasks.expire_invitation_codes"
    ]
}
