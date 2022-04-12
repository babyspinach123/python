import json 

person_dict= {'first':'Thomas','last':'Knight'}
person_dict['city']= 'nottingham'
person_dict['hobbies'] = ['mountain biking','rc cars','xbox'] 
print(person_dict)

person_json=json.dumps(person_dict)

print(person_json)

address_book_list=[]
address_book_entry_dict={'id':'1','person':person_dict}
address_book_list.append(address_book_entry_dict)
address_book_entry_dict={'id':'2','person':{}}
address_book_list.append(address_book_entry_dict)

print(json.dumps(address_book_list))

