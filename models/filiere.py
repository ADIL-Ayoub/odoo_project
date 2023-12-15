from odoo import api, models, fields


class Filiere(models.Model):
    _name = 'abscence.filiere'
    _description = 'Classe pour gérer les filières'
    _rec_name = 'libelle'

    libelle = fields.Char(string='Libellé', required=True)
    matieres = fields.One2many(
        'abscence.matiere', 'filiere_id', string='Matieres')
    etudiants = fields.One2many(
        'abscence.etudiant', 'filiere_id', string='Etudiants')
