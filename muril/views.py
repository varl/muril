##
## Multi Uniform Resource Index Locator
##

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render_to_response
from muril.models import Link

def index(request):
	return HttpResponse("Hello world")

def expand_link(request, link_id):
	link = get_object_or_404(Link, pk=link_id)
	link_dict = link.link.split(',')
	return render_to_response('expand_link.html',
				  locals(),
				  context_instance=RequestContext(request))
