import math


def pagination(form, page, limit):
    return {
            "current_page": page,
            "limit": limit,
            "pages": math.ceil(form.count() / limit),
            "data": form.offset((page) * limit).limit(limit).all()
            }

def pagination2(data,search,page,limit):
    
    # apply search filter if necessary
    if search:
        query = query.filter(data.name.like(f'%{search}%'))
    
    # order the query by customer name
    query = query.order_by(data.name.asc())
    
    # calculate offset and limit based on page and limit values
    offset = (page - 1) * limit
    if offset < 0:
        offset = 0
    query = query.offset(offset).limit(limit)
    
    return query.all()