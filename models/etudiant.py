from odoo import api, models, fields


class Etudiant(models.Model):
    _name = 'abscence.etudiant'
    _description = 'Classe pour gérer les étudiants'
    _rec_name = 'nom_prenom'

    nom = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string='Prénom', required=True)
    email = fields.Char(string='Email', required=True)
    password = fields.Char(string='Mot de passe', required=True)
    tele = fields.Char(string='Téléphone')
    cin = fields.Char(string='CIN', required=True)
    filiere_id = fields.Many2one('abscence.filiere', string='Filière')
    temp = fields.Char(string='temp',
                       compute='_compute_nom_prenom', store=True)

    # matieres = fields.Many2many('abscence.matiere', string='Matieres')

    # A computed field combining nom and prenom for _rec_name
    nom_prenom = fields.Char(string='Nom et Prénom',
                             compute='_compute_nom_prenom', store=True)

    @api.depends('nom', 'prenom')
    def _compute_nom_prenom(self):
        for record in self:
            record.nom_prenom = f"{record.nom} {record.prenom}"

    @api.depends('nom', 'prenom')
    def _compute_nom_prenom(self):
        for record in self:
            record.temp = f"{self.env.user.email}"
