import cobra.test
import pandas as pd
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit
import numpy as np
import seaborn as sns
import os
import math
from os.path import join
from cobra import Model, Reaction, Metabolite
from cobra.io import save_json_model
from progressbar import ProgressBar


# Load data from Fig 4 of Khula and Oelze

Fig4_data = pd.read_csv("../Data/Experimental_Data/Khula_Oelze_1988_Figure_4.csv")
# print(len(Fig4_data))


# load ATPM predictions
ATPM_pred = pd.read_csv("../Data/Maintenance_rates/Maintenance_rates_pred.csv", index_col=0)
ATPM_pred.rename({'O2_concentration': 'Oxygen_conc', 'ATPM_bound_value': 'ATPM_pred'}, axis=1, inplace=True)
# print(len(ATPM_pred))


# Merge ATPM predictions and experimental data

ATPM_pred_merge = pd.merge(left=ATPM_pred, right=Fig4_data, left_on='Oxygen_conc', right_on='Oxygen_conc')
ATPM_pred_merge.to_csv("../Data/Maintenance_rates/ATPM_pred_merge.csv")
# print(ATPM_pred_merge.head(50))

# reaction ids not in pathway then "name" of pathway
NII_BD_F = ["NADH6", "CYOO2pp", "RNF", "NII_BD_F"]
NII_CO_F = ["NADH6", "CYTBDpp", "RNF", "NII_CO_F"]
NII_BD_R = ["NADH6", "CYOO2pp", "FIX", "NII_BD_R"]
NII_CO_R = ["NADH6", "CYTBDpp", "FIX", "NII_CO_R"]
NI_BD_F = ["NADH5", "CYOO2pp", "RNF", "NI_BD_F"]
NI_CO_F = ["NADH5", "CYTBDpp", "RNF", "NI_CO_F"]
NI_BD_R = ["NADH5", "CYOO2pp", "FIX", "NI_BD_R"]
NI_CO_R= ["NADH5", "CYTBDpp", "FIX", "NI_CO_R"]

all_paths = [NII_BD_F,
                NII_CO_F,
                NII_BD_R,
                NII_CO_R,
                NI_BD_F,
                NI_CO_F,
                NI_BD_R,
                NI_CO_R]


def metabolite_flux_balance(metabolite, solution):
    """
    Return a vector of reaction fluxes scaled by the stoichiometric coefficient.

    Parameters
    ----------
    metabolite : cobra.Metabolite
        The metabolite whose fluxes are to be investigated.
    solution : cobra.Solution
        Solution with flux values.

    Returns
    -------
    pandas.Series
        A vector with fluxes of reactions that consume or produce the given
        metabolite scaled by the corresponding stoichiometric coefficients. The
        reaction identifiers are given by the index.
    """
    rxn_ids = list()
    rxn_sub = list()
    adj_flux = list()
    for rxn in metabolite.reactions:
        coef = rxn.get_coefficient(metabolite)
        rxn_ids.append(rxn.id)
        rxn_sub.append(rxn.subsystem)
        adj_flux.append(coef * solution.fluxes[rxn.id])
    return pd.DataFrame({'Rxn_id': rxn_ids, 'Subsystem': rxn_sub, 'Adjusted_Flux': adj_flux})


# Two functions that will pull the total ATP produced and the ratio of ATPM/Total ATP from the above function
def ATP_total(df):
    positive_num = df[(df.Adjusted_Flux > 0)]
    ATP_total = positive_num['Adjusted_Flux'].sum()

    return ATP_total


def ATP_ratio(df, ATP_total):
    ATPM = df.loc[df['Rxn_id'] == 'ATPM', 'Adjusted_Flux'].values[0]
    ATPM_ratio = (ATPM * -1) / ATP_total

    return ATPM_ratio


def growth_yeild(u_exp, u_pred, uptake_exp):
    growth_yeild_exp = u_exp / (uptake_exp / 1000)
    growth_yeild_pred = u_pred / (uptake_exp / 1000)

    return growth_yeild_exp, growth_yeild_pred


# def calc_max_growth_yeild(u_exp, u_pred, uptake_exp):

# function for pulling single row of data

def
