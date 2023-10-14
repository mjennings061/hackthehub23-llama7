from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .forms import TriageForm
from .order_of_events import get_order_of_events
from .generate_diagram import get_generated_image
from .extract_highway_sections import return_answer_and_sections


# TODO: Create an index that renders a form for the user to enter their transcript.
def index(request):
    """Render a form for the user to enter their transcript."""
    form = TriageForm()
    return render(request, 'triage_form.html', {'form': form})

def view_report(request):
    """Render a report based on the user's transcript."""
    if request.method == 'POST':
        form = TriageForm(request.POST)
        if not form.is_valid():
            # Process the form data (e.g., save it to the database)
            # Redirect to a success page or perform other actions
            return
        
    # Get the name from the POST request.
    name = request.POST['name']
        
    # Get the transcript from the POST request.
    transcript = request.POST['transcript']

    # Get the order of events from the transcript.
    order_of_events = get_order_of_events(transcript=transcript)

    # Get the related articles from the order of events.
    answer, related_articles = return_answer_and_sections(order_of_events)
    print(related_articles)

    # Get the image from the order of events.
    image = get_generated_image(order_of_events=order_of_events)

    # Render the template.
    template = loader.get_template('view_report.html')
    context = {
        'name': name,
        'diagram': image,
        'order_of_events': order_of_events,
        'related_articles': related_articles,
        'answer': answer,
        'transcript': transcript,
    }
    return HttpResponse(template.render(context, request))

