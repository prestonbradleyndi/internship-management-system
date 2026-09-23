from odoo import http
from odoo.http import request


class InternshipPortal(http.Controller):

    @http.route(
        '/my/internship',
        type='http',
        auth='user',
        website=True
    )
    def internship_dashboard(self, **kwargs):

        user = request.env.user

        intern = request.env['ims.intern'].sudo().search(
            [('email', '=', user.email)],
            limit=1
        )

        if not intern:
            return request.not_found()

        tasks = request.env['ims.task'].sudo().search(
            [('intern_id', '=', intern.id)]
        )

        reports = request.env['ims.internship.report'].sudo().search(
            [('intern_id', '=', intern.id)]
        )

        feedback = request.env['ims.feedback'].sudo().search(
            [('intern_id', '=', intern.id)]
        )

        supervisor = False

        if intern.supervisor_id:
            supervisor = intern.supervisor_id.sudo()

        return request.render(
            'internship_portal.portal_dashboard',
            {
                'intern': intern,
                'tasks': tasks,
                'reports': reports,
                'feedback': feedback,
                'supervisor': supervisor,
            }
        )