from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Category

def index(request):
    # On first load, check if Category A and Category B exist
    category_a, created_a = Category.objects.get_or_create(name="Category A", parent=None)
    category_b, created_b = Category.objects.get_or_create(name="Category B", parent=None)
    context={
        'category_a_id': category_a.id,
        'category_b_id': category_b.id,
    }
    return render(request, 'index.html', context)

def create_subcategories(request):
    if request.method == 'POST':
        parent_id = request.POST.get('parent_id')
        parent_category = get_object_or_404(Category, id=parent_id)

        # Get how many subcategories exist for this parent to follow naming convention
        existing_subcategories = parent_category.children.all()
        next_subcategory_number = existing_subcategories.count() + 1

        # Create two new subcategories for the selected category
        subcategory1 = Category.objects.create(
            name=f"SUB {parent_category.name}{next_subcategory_number}",
            parent=parent_category
        )
        subcategory2 = Category.objects.create(
            name=f"SUB {parent_category.name}{next_subcategory_number + 1}",
            parent=parent_category
        )

        # Return the two created subcategories
        return JsonResponse({
            'subcategories': [
                {'id': subcategory1.id, 'name': subcategory1.name},
                {'id': subcategory2.id, 'name': subcategory2.name},
            ]
        })

    return JsonResponse({'error': 'Invalid request'}, status=400)
