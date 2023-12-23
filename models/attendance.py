from odoo import api, models, fields


class Attendance(models.Model):
    _name = 'abscence.attendance'
    _description = 'Attendance'
    _rec_name = 'libelle'

    libelle = fields.Char(string='Libelle', required=True)
    current_date = fields.Date(
        string="Date de création", default=fields.Date.today)
    professor_id = fields.Many2one(
        'abscence.professeur', string='Professeur')
    subject_ids = fields.Many2many(
        'abscence.matiere', string='Matieres', store=True
        # , compute="_compute_subjects"
    )
    etudiants_ids = fields.Many2many(
        'abscence.etudiant', string='Etudiants', store=True
        # , compute="_compute_etudiants"
    )
    subject_names = fields.Char(
        string='Subject Names', compute='_compute_subject_names', store=True)

    @api.depends('subject_ids')
    def _compute_subject_names(self):
        for record in self:
            record.subject_names = ', '.join(
                record.subject_ids.mapped('libelle'))

    etudiants_count_per_subject = fields.Integer(
        string='Number of Students per Subject', compute='_compute_etudiants_count_per_subject', store=True)

    @api.depends('etudiants_ids')
    def _compute_etudiants_count_per_subject(self):
        for record in self:
            record.etudiants_count_per_subject = len(record.etudiants_ids)

    @ api.onchange('professor_id')
    def onchange_professor_id(self):
        """
        Compute the subjects related to the selected professor.
        """
        for record in self:
            if record.professor_id:
                # Update the domain for the subject_ids field
                record.subject_ids = record.professor_id.matieres
            else:
                # Clear the subjects if no professor is selected
                record.subject_ids = [(5, 0, 0)]

    @ api.onchange('subject_ids')
    def onchange_subject_ids(self):
        """
        Compute the subjects related to the selected professor.
        """
        for record in self:
            if record.subject_ids:
                for sub in record.subject_ids:
                    record.etudiants_ids = sub.filiere_id.etudiants
            else:
                # Clear the subjects if no professor is selected
                record.etudiants_ids = [(5, 0, 0)]


# for record in self:
#             if record.subject_ids:
#                 for sub in record.subject_ids:

#                     students = sub.filiere_id.etudiants
#                     for student in students:
#                         if student not in self.etudiants_ids.ids:
#                             self.etudiants_ids = [(4, student, 0)]
