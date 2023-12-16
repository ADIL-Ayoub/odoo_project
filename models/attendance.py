from odoo import api, models, fields


class Attendance(models.Model):
    _name = 'abscence.attendance'
    _description = 'Attendance'
    _rec_name = 'libelle'

    libelle = fields.Char(string='Libelle', required=True)
    professor_id = fields.Many2one(
        'abscence.professeur', string='Professeur')
    subject_ids = fields.Many2many('abscence.matiere', string='Matieres')

    @api.depends('professor_id')
    def _compute_subjects(self):
        """
        Compute the subjects related to the selected professor.
        """
        for record in self:
            if record.professor_id:
                # Update the domain for the subject_ids field
                record.subject_ids = [
                    (6, 0, record.professor_id.matieres)]
            else:
                # Clear the subjects if no professor is selected
                record.subject_ids = [(5, 0, 0)]
