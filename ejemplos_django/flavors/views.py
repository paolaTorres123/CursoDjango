import json
from django.contrib import messages
from django.core import serializers
from core.models import ModelFormFailureHistory


class FlavorActionMixin:
    @property
    def success_msg(self):
        return NotImplemented
    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super(FlavorActionMixin, self).form_valid(form)
    
    def form_invalid(self, form):
        """Save invalid form and model data for later reference."""
        form_data = json.dumps(form.cleaned_data)
        # Serialize the form.instance
        model_data = serializers.serialize('json', [form.instance])
        # Strip away leading and ending bracket leaving only a dict
        model_data = model_data[1:-1]
        ModelFormFailureHistory.objects.create(
            form_data=form_data,
            model_data=model_data
        )
        return super(FlavorActionMixin,
                    self).form_invalid(form)