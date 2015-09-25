# This script is used to compare .txt files consisting of lists
# of reports, and return the ones that were missing and added.

def compare (last_month,this_month):

    missing = []
    added = []
    last_list = []
    this_list = []
    
    for item in last_month:

        if '#TYPE System.Data.DataRow' in item or '"resource_name","context","filename","filesize"' in item:
            pass        
        else:           
            last_data = item.strip()
            last_data = last_data.split(',')
            last_list.append(last_data[0])

    for item in this_month:

        if '#TYPE System.Data.DataRow' in item or '"resource_name","context","filename","filesize"' in item:
            pass        
        else:             
            this_data = item.strip()
            this_data = this_data.split(',')        
            this_list.append(this_data[0])

    print('Reports last month:',len(last_list))
    print('Reports this month:',len(this_list))
    print('--------------------------------------------\n')

    for item in range(0,len(last_list)):
        if last_list[item] not in this_list:
            missing.append(last_list[item])
        else:
            pass

    for item in range(0,len(this_list)):
        if this_list[item] not in last_list:
            added.append(this_list[item])
        else:
            pass       

    return missing, added

def main():

    last_month = open('jan_rpts.txt','r')
    this_month = open ('feb_rpts.txt','r')

    missing, added = compare(last_month,this_month)

    if missing == []:
        print('There are no missing reports.\n')
    if added == []:
        print('There are no added reports.\n')
    if missing != []:
        print('Missing reports:\n')
        for item in range(0,len(missing)):
            print('\t',missing[item],'\n')
    if added != []:
        print('Added reports:\n')
        for item in range(0,len(added)):
            print('\t',added[item],'\n')        

main()
