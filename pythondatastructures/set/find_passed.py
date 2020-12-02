total_list=['arun','vijay','ajay','ajith','james','jonny','jimmy']
passed_list=['vijay','ajith','jonny','ajay']
total_list=set(total_list)
passed_list=set(passed_list)
failed_list=list(total_list.difference(passed_list))
print(failed_list)