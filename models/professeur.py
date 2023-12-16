from odoo import api, models, fields


class Professeur(models.Model):
    _name = 'abscence.professeur'
    _description = 'Classe pour gérer les professeurs'
    _rec_name = 'nom'
    nom = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string='Prénom', required=True)
    email = fields.Char(string='Email', required=True)
    password = fields.Char(string='Mot de passe', required=True)
    tele = fields.Char(string='Téléphone')
    cin = fields.Char(string='CIN', required=True)
    matieres = fields.One2many(
        'abscence.matiere', 'professeur_id', string='Matieres')
    
