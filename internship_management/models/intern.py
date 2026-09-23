from odoo import models, fields, api


class ResUsers(models.Model):
    _inherit = 'res.users'

    can_be_ims_supervisor = fields.Boolean(
        string='Can Be Assigned as Supervisor',
        default=False
    )


class Intern(models.Model):
    _name = 'ims.intern'
    _description = 'Intern'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    school = fields.Char(string='School')
    program = fields.Char(string='Program')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')

    supervisor_id = fields.Many2one(
        'res.users',
        string='Assigned Supervisor',
        domain=[('can_be_ims_supervisor', '=', True)]
    )

    status = fields.Selection([
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('terminated', 'Terminated'),
    ], string='Status', default='active')


class Internship(models.Model):
    _name = 'ims.internship'
    _description = 'Internship'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    department = fields.Char(string='Department')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')

    status = fields.Selection([
        ('planned', 'Planned'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='planned')


class Task(models.Model):
    _name = 'ims.task'
    _description = 'Internship Task'

    name = fields.Char(
        string='Task Title',
        required=True
    )

    description = fields.Text(
        string='Description'
    )

    assigned_date = fields.Date(
        string='Assigned Date'
    )

    due_date = fields.Date(
        string='Due Date'
    )

    status = fields.Selection([
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ],
        string='Status',
        compute='_compute_progress_and_status',
        store=True
    )

    progress = fields.Integer(
        string='Progress (%)',
        compute='_compute_progress_and_status',
        store=True
    )

    intern_id = fields.Many2one(
        'ims.intern',
        string='Intern',
        required=True
    )

    supervisor_id = fields.Many2one(
        'res.users',
        string='Supervisor'
    )

    internship_id = fields.Many2one(
        'ims.internship',
        string='Internship',
        required=True
    )

    subtask_ids = fields.One2many(
        'ims.task.subtask',
        'task_id',
        string='Subtasks'
    )

    @api.depends('subtask_ids.completed')
    def _compute_progress_and_status(self):
        for task in self:
            total_subtasks = len(task.subtask_ids)
            completed_subtasks = len(
                task.subtask_ids.filtered(lambda subtask: subtask.completed)
            )

            if total_subtasks == 0:
                task.progress = 0
                task.status = 'pending'
            else:
                task.progress = round(
                    (completed_subtasks / total_subtasks) * 100
                )

                if task.progress >= 100:
                    task.progress = 100
                    task.status = 'completed'
                elif task.progress > 0:
                    task.status = 'in_progress'
                else:
                    task.status = 'pending'


class TaskSubtask(models.Model):
    _name = 'ims.task.subtask'
    _description = 'Internship Task Subtask'

    name = fields.Char(
        string='Subtask',
        required=True
    )

    completed = fields.Boolean(
        string='Completed',
        default=False
    )

    task_id = fields.Many2one(
        'ims.task',
        string='Task',
        required=True,
        ondelete='cascade'
    )


class Attendance(models.Model):
    _name = 'ims.attendance'
    _description = 'Intern Attendance'

    intern_id = fields.Many2one(
        'ims.intern',
        string='Intern',
        required=True
    )

    date = fields.Date(
        string='Date',
        required=True
    )

    check_in_time = fields.Float(
        string='Check In'
    )

    check_out_time = fields.Float(
        string='Check Out'
    )

    status = fields.Selection([
        ('present', 'Present'),
        ('late', 'Late'),
        ('absent', 'Absent'),
    ], string='Status', default='present', required=True)

    notes = fields.Text(
        string='Notes'
    )


class InternshipReport(models.Model):
    _name = 'ims.internship.report'
    _description = 'Internship Report'

    name = fields.Char(
        string='Report Title',
        required=True
    )

    intern_id = fields.Many2one(
        'ims.intern',
        string='Intern',
        required=True
    )

    internship_id = fields.Many2one(
        'ims.internship',
        string='Internship',
        required=True
    )

    submission_date = fields.Date(
        string='Submission Date'
    )

    file_path = fields.Char(
        string='File Path'
    )

    status = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('reviewed', 'Reviewed'),
    ], string='Status', default='draft', required=True)


class Evaluation(models.Model):
    _name = 'ims.evaluation'
    _description = 'Intern Evaluation'

    intern_id = fields.Many2one(
        'ims.intern',
        string='Intern',
        required=True
    )

    supervisor_id = fields.Many2one(
        'res.users',
        string='Supervisor',
        required=True
    )

    score = fields.Float(
        string='Score'
    )

    comments = fields.Text(
        string='Comments'
    )

    evaluation_date = fields.Date(
        string='Evaluation Date'
    )


class Feedback(models.Model):
    _name = 'ims.feedback'
    _description = 'Intern Feedback'

    intern_id = fields.Many2one(
        'ims.intern',
        string='Intern',
        required=True
    )

    supervisor_id = fields.Many2one(
        'res.users',
        string='Supervisor',
        required=True
    )

    comment = fields.Text(
        string='Feedback',
        required=True
    )

    date = fields.Date(
        string='Date'
    )