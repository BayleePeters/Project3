#import the required modules
import pandas as pd
import numpy as np

#create new data frame from CSV for beginning inventory
beginvDF = pd.read_csv("D:\ACC470\BegInvFINAL.csv")

#aggregate records in the beginning inventory data frame by grouping inventory ID and sum each quantity
beginvDF = beginvDF.groupby("InventoryId").sum()
beginvDF = beginvDF.reset_index()

#create a new data frame for aggregate data, beginning inventory balances and inventory IDs
aggbeginvDF = beginvDF[["InventoryId", "onHand"]]

#Rename column header for onHand to BegQty
aggbeginvDF = aggbeginvDF.rename(columns={"onHand":"BegQty"})

#create new data frame from CSV for purchases
purchasesDF = pd.read_csv("D:\ACC470\purchasesFINAL.csv")

#aggregate records in the purchases data frame by grouping inventory ID and sum each quantity
purchasesDF = purchasesDF.groupby("InventoryId").sum()
purchasesDF = purchasesDF.reset_index()

#create a new data frame for aggregate data, quantities purchased and inventory IDs
aggpurchasesDF = purchasesDF[["InventoryId", "Quantity"]]

#Rename column header for Quantity to PurchQty
aggpurchasesDF = aggpurchasesDF.rename(columns={"Quantity":"PurchQty"})

#create new data frame from CSV for sales
salesDF = pd.read_csv("D:\ACC470\salesFINAL.csv")

#aggregate records in the sales data frame by grouping inventory ID and sum each quantity
salesDF = salesDF.groupby("InventoryId").sum()
salesDF = salesDF.reset_index()

#create a new data frame for aggregate data, quantities sold and inventory IDs
aggsalesDF = salesDF[["InventoryId", "SalesQuantity"]]

#Rename column header for SalesQuantity to SalesQty
aggsalesDF = aggsalesDF.rename(columns={"SalesQuantity":"SalesQty"})

#create new data frame from CSV for ending inventory
endinvDF = pd.read_csv("D:\ACC470\EndInvFINAL.csv")

#aggregate records in the ending inventory data frame by grouping inventory ID and sum each quantity
endinvDF = endinvDF.groupby("InventoryId").sum()
endinvDF = endinvDF.reset_index()

#create a new data frame for aggregate data, onHand and inventory IDs
aggendinvDF = endinvDF[["InventoryId", "onHand"]]

#Rename column header for onHand to EndQty
aggendinvDF = aggendinvDF.rename(columns={"onHand":"EndQty"})

#merge beginning inventory and purchases data frames on InventoryID
merged1DF = pd.merge(aggbeginvDF, aggpurchasesDF, on = "InventoryId", how = "outer")

#merge merged1 and sales data frames on InventoryID
merged2DF = pd.merge(merged1DF, aggsalesDF, on = "InventoryId", how = "outer")

#merge merged2 and ending inventory data framess on InventoryID
finalmergedDF = pd.merge(merged2DF, aggendinvDF, on = "InventoryId", how = "outer")

#create a new column is the merged data frame for difference
finalmergedDF["Diff"] = finalmergedDF["BegQty"] + finalmergedDF["PurchQty"] - finalmergedDF["SalesQty"] - finalmergedDF["EndQty"]

#display sum of the Diff colmun to the user
total = finalmergedDF["Diff"].sum()
total = round(total)
print ("The total Difference is " + str(total))

#display the total ending inventory to the user
print ("The total ending inventory for Bibitor LLC is " + str(finalmergedDF.shape[0]))





