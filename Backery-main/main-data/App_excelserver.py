import pandas as pd
def load_data(file_path):
    data = []
    try:
        df = pd.read_excel(file_path)
        for index, row in df.iterrows():
            image_path = row['Image']
            food_name = row['Food']  # Adjusted column name
            price = row['Price']  # Adjusted column name
            data.append((image_path, food_name, price))
        return data
    except Exception as e:
        print("error :",e)
        return data

def save_order(image_path, food_name, price, food_id,user,doo,ph,addr):
    with open ('store.txt','r+') as f:
        username=f.read()
    order_data = {
        "User Name":[username],
        "Food ID": [food_id],
        "Image Path": [image_path],
        "Food Name": [food_name],
        "Price": [price],
        "User":[user],
        "Date_order":[doo],
        "Phone no":[ph],
        "Address":[addr],
        "Delivery Status":["no"]
    }
    try:
        df = pd.DataFrame(order_data)
        existing_df = pd.read_excel("App-oder_data.xlsx")
        df = pd.concat([existing_df, df], ignore_index=True)
    except FileNotFoundError:
        print("Exception : file not found.")
    df.to_excel("App-oder_data.xlsx", index=False)
    


def load_order(file_path, username):
    data = []
    try:
        df = pd.read_excel(file_path)
        df_filtered = df[df['User Name'] == username]
        for index, row in df_filtered.iterrows():
            food_id = row['Food ID']
            image_path = row['Image Path']
            food_name = row['Food Name']
            price = row['Price']
            user = row['User']
            date_order = row['Date_order']
            ph = row['Phone no']
            addr = row['Address']
            data.append((food_id, image_path, food_name, price, user, date_order, ph, addr))
        return data
    except Exception as e:
        print("Exception : ",e)
        return data

def trackorder(file_path, fid, user_n):
    data = []
    try:
        df = pd.read_excel(file_path)
        df_filtered = df[(df['Food ID'] == fid) & (df['User Name'] == user_n)]
        for index, row in df_filtered.iterrows():
            food_id = row['Food ID']
            image_path = row['Image Path']
            food_name = row['Food Name']
            price = row['Price']
            user = row['User']
            date_order = row['Date_order']
            ph = row['Phone no']
            addr = row['Address']
            status=row['Delivery Status']
            data.append((food_id, image_path, food_name, price, user, date_order, ph, addr,status))
        return data
    except Exception as e:
        print("Exception:", e)
        return data

def cancel_order(file_path, fid, user):
    try:
        df = pd.read_excel(file_path)
        df_filtered = df[~((df['Food ID'] == fid) & (df['User Name'] == user))]
        df_filtered.to_excel(file_path, index=False)      
        print(f"Order Cancel, where Food ID {fid} and User {user}")
        return df_filtered
    except Exception :
        print("make sure your excel file is close")
        return False
    
    
def cancel_all(file_path, user_name):
    df_filtered = None
    try:
        df = pd.read_excel(file_path)
        df_filtered = df[df['User Name'] != user_name]
        df_filtered.to_excel(file_path, index=False)
        print(f"User details deleted for user: {user_name}")
        return df_filtered 
    except Exception as e:
        return df_filtered

