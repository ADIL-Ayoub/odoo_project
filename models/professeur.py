from odoo import api, models, fields


class Professeur(models.Model):
    _name = 'abscence.professeur'
    _description = 'Classe pour gérer les professeurs'
    _rec_name = 'nom_prenom'

    nom = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string='Prénom', required=True)
    nom_prenom = fields.Char(string='Nom et Prénom',
                             compute='_compute_nom_prenom', store=True)
    email = fields.Char(string='Email', required=True)
    password = fields.Char(string='Mot de passe', required=True)
    tele = fields.Char(string='Téléphone')
    cin = fields.Char(string='CIN', required=True)
    matieres = fields.One2many(
        'abscence.matiere', 'professeur_id', string='Matieres')
    current_date = fields.Date(
        string="Date de création", default=fields.Date.today)

    @api.depends('nom', 'prenom')
    def _compute_nom_prenom(self):
        for record in self:
            record.nom_prenom = f"{record.nom} {record.prenom}"
