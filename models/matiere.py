from odoo import api, models, fields


class Matiere(models.Model):
    _name = 'abscence.matiere'
    _description = 'Classe pour gérer les matières'
    _rec_name = 'libelle'

    libelle = fields.Char(string='Libellé', required=True)
    professeur_id = fields.Many2one(
        'abscence.professeur', string='Professeur')
    filiere_id = fields.Many2one('abscence.filiere', string='Filière')
    current_date = fields.Date(
        string="Date de création", default=fields.Date.today)
