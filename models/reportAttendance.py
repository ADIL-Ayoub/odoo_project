from odoo import api, models


class ReportAttendance(models.AbstractModel):
    _name = 'abscence.report_attendance'
    _description = 'Attendance Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        # Assuming docids contains the IDs of the Attendance records for which the report is generated
        docs = self.env['abscence.attendance'].browse(docids)
        return {
            'docs': docs,
        }
