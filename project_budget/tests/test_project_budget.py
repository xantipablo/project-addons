# Copyright 2018 Oihane Crucelaegui - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo.tests import common
from odoo import exceptions, fields

from_string = fields.Date.from_string
to_string = fields.Date.to_string


class TestProjectBudget(common.SavepointCase):

    @classmethod
    def setUpClass(cls):
        super(TestProjectBudget, cls).setUpClass()
        project_model = cls.env['project.project']
        cls.project = project_model.create({
            'name': 'New Project'
        })

    def test_project_creation(self):
        self.assertTrue(self.project.budget_ids)
        self.assertTrue(self.project.budget_ids[:1].initial)
        self.assertEquals(
            len(self.project.budget_ids), self.project.budget_count)
        self.assertEquals(len(
            self.project.mapped('budget_ids.crossovered_budget_line')), 26)
        self.project.create_initial_project_budget()
        self.assertEquals(len(self.project.budget_ids), 1)

    def test_initial_budget_per_project_year(self):
        new_budget = self.project.budget_ids.copy()
        with self.assertRaises(exceptions.ValidationError):
            new_budget.initial = True

    def test_budget_line_creation(self):
        new_budget = self.project.budget_ids.copy(default={
            'crossovered_budget_line': [],
        })
        new_budget.date_to = from_string(fields.Date.today()).replace(
            month=12, day=29)
        new_budget.action_create_period()
        self.assertEquals(len(
            new_budget.crossovered_budget_line), 24)
