from odoo import api, models, fields


class Attendance(models.Model):
    _name = 'abscence.attendance'
    _description = 'presence'
    _rec_name = 'libelle'

    libelle = fields.Char(string='Libelle', required=True)
    current_date = fields.Date(
        string="Date de création", default=fields.Date.today)
    professor_id = fields.Many2one(
        'abscence.professeur', string='Professeur')
    subject_ids = fields.Many2many(
        'abscence.matiere', string='Matieres', store=True
    )
    etudiants_ids = fields.Many2many(
        'abscence.etudiant', string='Etudiants', store=True
    )
    subject_names = fields.Char(
        string='Matiere', compute='_compute_libelle_matieres', store=True)

    @api.depends('subject_ids')
    def _compute_libelle_matieres(self):
        for record in self:
            record.subject_names = ', '.join(
                record.subject_ids.mapped('libelle'))

    cpt_etudiants_par_matiere = fields.Integer(
        string='Nombre des etudiants par matiere', compute='_compute_etudiants_par_matiere', store=True)

    @api.depends('etudiants_ids')
    def _compute_etudiants_par_matiere(self):
        for record in self:
            record.cpt_etudiants_par_matiere = len(record.etudiants_ids)

    @ api.onchange('professor_id')
    def onchange_professor_id(self):
        for record in self:
            if record.professor_id:
                record.subject_ids = record.professor_id.matieres
            else:
                record.subject_ids = [(5, 0, 0)]

    @ api.onchange('subject_ids')
    def onchange_subject_ids(self):
        for record in self:
            if record.subject_ids:
                for sub in record.subject_ids:
                    record.etudiants_ids = sub.filiere_id.etudiants
            else:
                record.etudiants_ids = [(5, 0, 0)]
