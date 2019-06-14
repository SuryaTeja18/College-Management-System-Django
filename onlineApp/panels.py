from __future__ import absolute_import, unicode_literals
from debug_toolbar.panels import DebugPanel
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from debug_toolbar import settings as dt_settings
from debug_toolbar.panels import Panel
from debug_toolbar.utils import (
    get_stack,
    get_template_info,
    render_stacktrace,
    tidy_stacktrace,
)
import os
import sys
import psutil

class SysInfo(DebugPanel):
    name = 'SysInfo'
    has_content = True

    @property
    def nav_title(self):
        return _('Sys Infos')

    @property
    def title(self):
        return _('Sys Info Panel')

    @property
    def content(self):
        context = []
        for process in list(psutil.process_iter()):
            temp = [process.pid, process.name,process.memory_info().wset,process.memory_info().vms]
            context.append(temp)
        return render_to_string('sysinfoPanel.html',{'pid':str(os.getpid()),'sysPath':str(sys.path),'context':context})