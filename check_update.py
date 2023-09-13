# Function to check for updates or new stocks
def check_for_updates(previous_data):
    try:
        current_data = get_data()
        #display(current_data)
        if current_data.empty:
            print("no data")
            return previous_data  # If current_data is empty, return previous_data

        new_rcp_no = list(set(current_data['보고서 번호']) - set(previous_data['보고서 번호']))
        if new_rcp_no:
            # New data with new rcp_no has been created
            for rcp_no in new_rcp_no:
                new_data = current_data[current_data['보고서 번호'] == rcp_no]
                bot_msg(new_data)
  
                display(new_data)  # Replace display with print to show the new data
        

        return current_data

    except Exception as e:
        print(f"Error occurred while checking for updates: {e}")
        return previous_data
