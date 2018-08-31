# we get retings from Adou and Nisha to evaluate a mean on selected comments

df_rate_pl = pandas.read_csv("path_des_restos_notes_negativement_par_Adou.csv", sep=";", encoding ="ISO-8859-1")
for i in range(df_rate_pl.shape[0]): # If Y.shape is (n,m), Y.shape[0] is n
    df_rate_pl.at[i, "nom_de_la_colonne_correspondant_aux_restos"] = df_rate_pl.at[i, "nom_de_la_colonne_correspondant_aux_restos"].lower() # lower() returns a copy of the string in which all case-based characters have been lowercased
    df_rate_pl.at[i, "nom_de_la_colonne_de_comentaires"] = df_rate_pl.at[i, "nom_de_la_colonne_de_comentaires"].replace("\r", "").replace("\n", " ") # df.at can only access a single value at a time