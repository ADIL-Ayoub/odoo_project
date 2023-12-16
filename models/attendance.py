from odoo import api, models, fields


class Attendance(models.Model):
    _name = 'abscence.attendance'
    _description = 'Attendance'
    _rec_name = 'libelle'

    libelle = fields.Char(string='Libelle', required=True)
    professor_id = fields.Many2one(
        'abscence.professeur', string='Professeur')
    subject_ids = fields.Many2many(
        'abscence.matiere', string='Matieres', store=True, group_operator="count"
        # , compute="_compute_subjects"
    )
    etudiants_ids = fields.Many2many(
        'abscence.etudiant', string='Etudiants', store=True
        # , compute="_compute_etudiants"
    )

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
