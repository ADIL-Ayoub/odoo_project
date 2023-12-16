from odoo import api, models, fields


class Attendance(models.Model):
    _name = 'abscence.attendance'
    _description = 'Attendance'
    _rec_name = 'libelle'

    libelle = fields.Char(string='Libelle', required=True)
    professor_id = fields.Many2one(
        'abscence.professeur', string='Professeur')
    subject_ids = fields.Many2many(
        'abscence.matiere', string='Matieres', compute="_compute_subjects")

    @api.depends('professor_id')
    def _compute_subjects(self):
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

            # if record.professor_id:
            #     # Set the domain for the product_id field based on the selected customer
            #     domain = [('id', 'in', record.professor_id.matieres)]
            #     # Retrieve the first product related to the customer (if any)
            #     first_subject = record.professor_id.matieres[:1]
            #     # Set the product_id field with the first product (if any)
            #     record.subject_ids = first_subject
            #     # Set the domain for the product_id field
            #     record.fields_get(['subject_ids'])[
            #         'subject_ids']['domain'] = domain
            # else:
            #     # Clear the product_id if no customer is selected
            #     record.subject_ids = False
