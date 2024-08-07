# streamlit_app/app.py

import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder

from models.orm_models import Session, RioItems
from crud.update import RioItemsUpdater     
from crud.read import RioItemsRead




# Streamlit app
def main():
    st.title("Rio Items Buy Frequency Updater")

    alda = RioItemsRead()
    update = RioItemsUpdater()

    result = alda.get_filtered_items()


    data = [{'id': item.id,  
                 'item number': item.item_number,
                 'description': item.description,
                 'buy_freq': item.buy_freq,
                 'del_time': item.del_time}
                 for item in result]
    

   

    # Check if data is not empty
    if len(data) > 0 and all(isinstance(item, dict) for item in data):
        # Convert data to DataFrame
        df = pd.DataFrame(data)

        # Display the editable grid
        gb = GridOptionsBuilder.from_dataframe(df)
        gb.configure_default_column(editable=False)
        gb.configure_column("buy_freq", editable=True,  cellStyle={'backgroundColor': 'lightgreen'})
        gb.configure_selection('single')
        grid_options = gb.build()

        grid_response = AgGrid(
            df,
            gridOptions=grid_options
        )

        selected_rows = grid_response["selected_rows"]

        #if selected_rows is not None:
         #   st.write(selected_rows.iloc[0,2])
          #  id = selected_rows.iloc[0, 0]
           # buy_freq = selected_rows.iloc[0, 2]
            #update.update_buy_freq(id, buy_freq)

        if selected_rows is not None:
            
            id = int(selected_rows.iloc[0, 0])
            buy_freq = int(selected_rows.iloc[0, 3])

            st.write(f"Selected ID: {id}, Buy Frequency: {buy_freq}")

            update.update_buy_freq(id, buy_freq)
            st.success("Buy frequency updated successfully!")
            
            st.write(str(buy_freq)+"-"+str(id))




    
if __name__ == "__main__":
    main()
