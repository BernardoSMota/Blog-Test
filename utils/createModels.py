from blog.models import Tag, Category

def create_tag(request):
    tag_id_list = []
    tags = request.getlist('tags', [])        
    for tag in tags:
        if not tag.isnumeric():
            tag, created = Tag.objects.get_or_create(title=tag) 
            tag_id_list.append(str(tag.id))
        else:
            tag_id_list.append(str(tag))
        
    return tag_id_list

def create_category(request):
    category = request.get('category')
    existing = True
    if not category.isnumeric():
        category, created = Category.objects.get_or_create(title=category)
        category_id = [str(category.id)]
        existing = False
    else:
        existing = True
        
    return category if existing else category_id
