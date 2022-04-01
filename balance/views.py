def edit_category_view(request, id):
    obj = get_object_or_404(Category, id=id)
    if request.method == "POST":
        form = forms.CategoryForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            obj.name = cd['category_name']
            obj.save()
            return redirect('category_list')
    else:
        initial_data = {'category_name': obj.name}
        form = forms.CategoryForm(initial=initial_data)
    ctx = {'form': form, 'cancel_url': reverse('category_list')}
    return render(request, 'mycalendar/form.html', ctx)

def add_category_view(request):
    if request.method == "POST":
        form = forms.CategoryForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            obj, created = Category.objects.get_or_create(name=cd['category_name'])
            # UWAGA - poniżej najpierw zrobiłbym obiekt pythonowy
            # a dopiero potem go zapisal
            #obj = Category(name=cd['category_name'])
            #obj.save()
            return redirect('category_list')