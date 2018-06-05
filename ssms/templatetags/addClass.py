from django import template
register = template.Library()

@register.filter(name='addcss')
def addcss(field, css):
   return field.as_widget(attrs={"class":css})

@register.filter(name='addplaceholder')
def addph(field, text):
   return field.as_widget(attrs={"placeholder":text})

@register.assignment_tag
def strtoarr(text,num_rows):
	str_to_arr = text.split(",")
	if num_rows == len(str_to_arr):
		str_to_arr = str_to_arr
	elif num_rows > len(str_to_arr):
		diff = num_rows-len(str_to_arr)
		for i in range(diff):
			str_to_arr.append("")
	elif num_rows < len(str_to_arr):
		str_to_arr = str_to_arr[0:num_rows]
	return str_to_arr



@register.assignment_tag
def checkTab(models_data_name, loop_counter):
	loop_counter =  "test_condition_"+str(loop_counter)
	if models_data_name == loop_counter:
		return "1"
	else:
		return "0"
	