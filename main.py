import pickle
import jsonify
import requests
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from flask import Flask, render_template, request

app = Flask(__name__, template_folder = 'templates')
model = pickle.load(open(r'ipl_score_prediction.pkl', 'rb'))

@app.route('/', methods = ['GET'])
def Home():
    return render_template('home.html')

standard_to = StandardScaler()

@app.route('/predict', methods = ['POST'])
def predict():
    if request.method == 'POST':
        
        batting_team = request.form['aa']
        if batting_team == 'Chennai Super Kings':
            batting_team_Chennai_Super_Kings = 1
            batting_team_Delhi_Capitals = 0
            batting_team_Gujarat_Lions = 0
            batting_team_Kings_XI_Punjab = 0
            batting_team_Kolkata_Knight_Riders = 0
            batting_team_Mumbai_Indians = 0
            batting_team_Rajasthan_Royals = 0
            batting_team_Rising_Pune_Supergiant = 0
            batting_team_Royal_Challengers_Bangalore = 0
            batting_team_Sunrisers_Hyderabad = 0
        elif batting_team == 'Delhi Capitals':
            batting_team_Chennai_Super_Kings = 0
            batting_team_Delhi_Capitals = 1
            batting_team_Gujarat_Lions = 0
            batting_team_Kings_XI_Punjab = 0
            batting_team_Kolkata_Knight_Riders = 0
            batting_team_Mumbai_Indians = 0
            batting_team_Rajasthan_Royals = 0
            batting_team_Rising_Pune_Supergiant = 0
            batting_team_Royal_Challengers_Bangalore = 0
            batting_team_Sunrisers_Hyderabad = 0
        elif batting_team == 'Gujarat Lions':
            batting_team_Chennai_Super_Kings = 0
            batting_team_Delhi_Capitals = 0
            batting_team_Gujarat_Lions = 1
            batting_team_Kings_XI_Punjab = 0
            batting_team_Kolkata_Knight_Riders = 0
            batting_team_Mumbai_Indians = 0
            batting_team_Rajasthan_Royals = 0
            batting_team_Rising_Pune_Supergiant = 0
            batting_team_Royal_Challengers_Bangalore = 0
            batting_team_Sunrisers_Hyderabad = 0
        elif batting_team == 'Kings XI Punjab':
            batting_team_Chennai_Super_Kings = 0
            batting_team_Delhi_Capitals = 0
            batting_team_Gujarat_Lions = 0
            batting_team_Kings_XI_Punjab = 1
            batting_team_Kolkata_Knight_Riders = 0
            batting_team_Mumbai_Indians = 0
            batting_team_Rajasthan_Royals = 0
            batting_team_Rising_Pune_Supergiant = 0
            batting_team_Royal_Challengers_Bangalore = 0
            batting_team_Sunrisers_Hyderabad = 0
        elif batting_team == 'Kolkata Knight Riders':
            batting_team_Chennai_Super_Kings = 0
            batting_team_Delhi_Capitals = 0
            batting_team_Gujarat_Lions = 0
            batting_team_Kings_XI_Punjab = 0
            batting_team_Kolkata_Knight_Riders = 1
            batting_team_Mumbai_Indians = 0
            batting_team_Rajasthan_Royals = 0
            batting_team_Rising_Pune_Supergiant = 0
            batting_team_Royal_Challengers_Bangalore = 0
            batting_team_Sunrisers_Hyderabad = 0
        elif batting_team == 'Mumbai Indians':
            batting_team_Chennai_Super_Kings = 0
            batting_team_Delhi_Capitals = 0
            batting_team_Gujarat_Lions = 0
            batting_team_Kings_XI_Punjab = 0
            batting_team_Kolkata_Knight_Riders = 0
            batting_team_Mumbai_Indians = 1
            batting_team_Rajasthan_Royals = 0
            batting_team_Rising_Pune_Supergiant = 0
            batting_team_Royal_Challengers_Bangalore = 0
            batting_team_Sunrisers_Hyderabad = 0
        elif batting_team == 'Rajasthan Royals':
            batting_team_Chennai_Super_Kings = 0
            batting_team_Delhi_Capitals = 0
            batting_team_Gujarat_Lions = 0
            batting_team_Kings_XI_Punjab = 0
            batting_team_Kolkata_Knight_Riders = 0
            batting_team_Mumbai_Indians = 0
            batting_team_Rajasthan_Royals = 1
            batting_team_Rising_Pune_Supergiant = 0
            batting_team_Royal_Challengers_Bangalore = 0
            batting_team_Sunrisers_Hyderabad = 0
        elif batting_team == 'Rising Pune Supergiant':
            batting_team_Chennai_Super_Kings = 0
            batting_team_Delhi_Capitals = 0
            batting_team_Gujarat_Lions = 0
            batting_team_Kings_XI_Punjab = 0
            batting_team_Kolkata_Knight_Riders = 0
            batting_team_Mumbai_Indians = 0
            batting_team_Rajasthan_Royals = 0
            batting_team_Rising_Pune_Supergiant = 1
            batting_team_Royal_Challengers_Bangalore = 0
            batting_team_Sunrisers_Hyderabad = 0
        elif batting_team == 'Royal Challengers Bangalore':
            batting_team_Chennai_Super_Kings = 0
            batting_team_Delhi_Capitals = 0
            batting_team_Gujarat_Lions = 0
            batting_team_Kings_XI_Punjab = 0
            batting_team_Kolkata_Knight_Riders = 0
            batting_team_Mumbai_Indians = 0
            batting_team_Rajasthan_Royals = 0
            batting_team_Rising_Pune_Supergiant = 0
            batting_team_Royal_Challengers_Bangalore = 1
            batting_team_Sunrisers_Hyderabad = 0
        elif batting_team == 'Sunrisers Hyderabad':
            batting_team_Chennai_Super_Kings = 0
            batting_team_Delhi_Capitals = 0
            batting_team_Gujarat_Lions = 0
            batting_team_Kings_XI_Punjab = 0
            batting_team_Kolkata_Knight_Riders = 0
            batting_team_Mumbai_Indians = 0
            batting_team_Rajasthan_Royals = 0
            batting_team_Rising_Pune_Supergiant = 0
            batting_team_Royal_Challengers_Bangalore = 0
            batting_team_Sunrisers_Hyderabad = 1
        
        bowling_team = request.form['ab']
        if bowling_team == 'Chennai Super Kings':
            bowling_team_Chennai_Super_Kings = 1
            bowling_team_Delhi_Capitals = 0
            bowling_team_Gujarat_Lions = 0
            bowling_team_Kings_XI_Punjab = 0
            bowling_team_Kolkata_Knight_Riders = 0
            bowling_team_Mumbai_Indians = 0
            bowling_team_Rajasthan_Royals = 0
            bowling_team_Rising_Pune_Supergiant = 0
            bowling_team_Royal_Challengers_Bangalore = 0
            bowling_team_Sunrisers_Hyderabad = 0
        elif bowling_team == 'Delhi Capitals':
            bowling_team_Chennai_Super_Kings = 0
            bowling_team_Delhi_Capitals = 1
            bowling_team_Gujarat_Lions = 0
            bowling_team_Kings_XI_Punjab = 0
            bowling_team_Kolkata_Knight_Riders = 0
            bowling_team_Mumbai_Indians = 0
            bowling_team_Rajasthan_Royals = 0
            bowling_team_Rising_Pune_Supergiant = 0
            bowling_team_Royal_Challengers_Bangalore = 0
            bowling_team_Sunrisers_Hyderabad = 0
        elif bowling_team == 'Gujarat Lions':
            bowling_team_Chennai_Super_Kings = 0
            bowling_team_Delhi_Capitals = 0
            bowling_team_Gujarat_Lions = 1
            bowling_team_Kings_XI_Punjab = 0
            bowling_team_Kolkata_Knight_Riders = 0
            bowling_team_Mumbai_Indians = 0
            bowling_team_Rajasthan_Royals = 0
            bowling_team_Rising_Pune_Supergiant = 0
            bowling_team_Royal_Challengers_Bangalore = 0
            bowling_team_Sunrisers_Hyderabad = 0
        elif bowling_team == 'Kings XI Punjab':
            bowling_team_Chennai_Super_Kings = 0
            bowling_team_Delhi_Capitals = 0
            bowling_team_Gujarat_Lions = 0
            bowling_team_Kings_XI_Punjab = 1
            bowling_team_Kolkata_Knight_Riders = 0
            bowling_team_Mumbai_Indians = 0
            bowling_team_Rajasthan_Royals = 0
            bowling_team_Rising_Pune_Supergiant = 0
            bowling_team_Royal_Challengers_Bangalore = 0
            bowling_team_Sunrisers_Hyderabad = 0
        elif bowling_team == 'Kolkata Knight Riders':
            bowling_team_Chennai_Super_Kings = 0
            bowling_team_Delhi_Capitals = 0
            bowling_team_Gujarat_Lions = 0
            bowling_team_Kings_XI_Punjab = 0
            bowling_team_Kolkata_Knight_Riders = 1
            bowling_team_Mumbai_Indians = 0
            bowling_team_Rajasthan_Royals = 0
            bowling_team_Rising_Pune_Supergiant = 0
            bowling_team_Royal_Challengers_Bangalore = 0
            bowling_team_Sunrisers_Hyderabad = 0
        elif bowling_team == 'Mumbai Indians':
            bowling_team_Chennai_Super_Kings = 0
            bowling_team_Delhi_Capitals = 0
            bowling_team_Gujarat_Lions = 0
            bowling_team_Kings_XI_Punjab = 0
            bowling_team_Kolkata_Knight_Riders = 0
            bowling_team_Mumbai_Indians = 1
            bowling_team_Rajasthan_Royals = 0
            bowling_team_Rising_Pune_Supergiant = 0
            bowling_team_Royal_Challengers_Bangalore = 0
            bowling_team_Sunrisers_Hyderabad = 0
        elif bowling_team == 'Rajasthan Royals':
            bowling_team_Chennai_Super_Kings = 0
            bowling_team_Delhi_Capitals = 0
            bowling_team_Gujarat_Lions = 0
            bowling_team_Kings_XI_Punjab = 0
            bowling_team_Kolkata_Knight_Riders = 0
            bowling_team_Mumbai_Indians = 0
            bowling_team_Rajasthan_Royals = 1
            bowling_team_Rising_Pune_Supergiant = 0
            bowling_team_Royal_Challengers_Bangalore = 0
            bowling_team_Sunrisers_Hyderabad = 0
        elif bowling_team == 'Rising Pune Supergiant':
            bowling_team_Chennai_Super_Kings = 0
            bowling_team_Delhi_Capitals = 0
            bowling_team_Gujarat_Lions = 0
            bowling_team_Kings_XI_Punjab = 0
            bowling_team_Kolkata_Knight_Riders = 0
            bowling_team_Mumbai_Indians = 0
            bowling_team_Rajasthan_Royals = 0
            bowling_team_Rising_Pune_Supergiant = 1
            bowling_team_Royal_Challengers_Bangalore = 0
            bowling_team_Sunrisers_Hyderabad = 0
        elif bowling_team == 'Royal Challengers Bangalore':
            bowling_team_Chennai_Super_Kings = 0
            bowling_team_Delhi_Capitals = 0
            bowling_team_Gujarat_Lions = 0
            bowling_team_Kings_XI_Punjab = 0
            bowling_team_Kolkata_Knight_Riders = 0
            bowling_team_Mumbai_Indians = 0
            bowling_team_Rajasthan_Royals = 0
            bowling_team_Rising_Pune_Supergiant = 0
            bowling_team_Royal_Challengers_Bangalore = 1
            bowling_team_Sunrisers_Hyderabad = 0
        elif bowling_team == 'Sunrisers Hyderabad':
            bowling_team_Chennai_Super_Kings = 0
            bowling_team_Delhi_Capitals = 0
            bowling_team_Gujarat_Lions = 0
            bowling_team_Kings_XI_Punjab = 0
            bowling_team_Kolkata_Knight_Riders = 0
            bowling_team_Mumbai_Indians = 0
            bowling_team_Rajasthan_Royals = 0
            bowling_team_Rising_Pune_Supergiant = 0
            bowling_team_Royal_Challengers_Bangalore = 0
            bowling_team_Sunrisers_Hyderabad = 1
                     
        toss_winner = request.form['ac']
        if toss_winner == batting_team:
            toss_decision_bat = 1
            toss_decision_field = 0
        elif toss_winner == bowling_team:
            toss_decision_bat = 0
            toss_decision_field = 1
            
        venue = request.form['ad']
        if venue == 'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium':
            venue_Dr_YS_Rajasekhara_Reddy_ACA_VDCA_Cricket_Stadium = 1
            venue_Dubai_International_Cricket_Stadium = 0
            venue_Eden_Gardens = 0
            venue_Feroz_Shah_Kotla = 0
            venue_Green_Park = 0
            venue_Holkar_Cricket_Stadium = 0
            venue_M_Chinnaswamy_Stadium = 0
            venue_MA_Chidambaram_Stadium_Chepauk = 0
            venue_Maharashtra_Cricket_Association_Stadium = 0
            venue_Punjab_Cricket_Association_IS_Bindra_Stadium_Mohali = 0
            venue_Rajiv_Gandhi_International_Stadium_Uppal = 0
            venue_Saurashtra_Cricket_Association_Stadium = 0
            venue_Sawai_Mansingh_Stadium = 0
            venue_Shaheed_Veer_Narayan_Singh_International_Stadium = 0
            venue_Sharjah_Cricket_Stadium = 0
            venue_Sheikh_Zayed_Stadium = 0
            venue_Wankhede_Stadium = 0
        if venue == 'Dubai International Cricket Stadium':
            venue_Dr_YS_Rajasekhara_Reddy_ACA_VDCA_Cricket_Stadium = 0
            venue_Dubai_International_Cricket_Stadium = 1
            venue_Eden_Gardens = 0
            venue_Feroz_Shah_Kotla = 0
            venue_Green_Park = 0
            venue_Holkar_Cricket_Stadium = 0
            venue_M_Chinnaswamy_Stadium = 0
            venue_MA_Chidambaram_Stadium_Chepauk = 0
            venue_Maharashtra_Cricket_Association_Stadium = 0
            venue_Punjab_Cricket_Association_IS_Bindra_Stadium_Mohali = 0
            venue_Rajiv_Gandhi_International_Stadium_Uppal = 0
            venue_Saurashtra_Cricket_Association_Stadium = 0
            venue_Sawai_Mansingh_Stadium = 0
            venue_Shaheed_Veer_Narayan_Singh_International_Stadium = 0
            venue_Sharjah_Cricket_Stadium = 0
            venue_Sheikh_Zayed_Stadium = 0
            venue_Wankhede_Stadium = 0
        elif venue == 'Eden Gardens':
            venue_Dr_YS_Rajasekhara_Reddy_ACA_VDCA_Cricket_Stadium = 0
            venue_Dubai_International_Cricket_Stadium = 0
            venue_Eden_Gardens = 1
            venue_Feroz_Shah_Kotla = 0
            venue_Green_Park = 0
            venue_Holkar_Cricket_Stadium = 0
            venue_M_Chinnaswamy_Stadium = 0
            venue_MA_Chidambaram_Stadium_Chepauk = 0
            venue_Maharashtra_Cricket_Association_Stadium = 0
            venue_Punjab_Cricket_Association_IS_Bindra_Stadium_Mohali = 0
            venue_Rajiv_Gandhi_International_Stadium_Uppal = 0
            venue_Saurashtra_Cricket_Association_Stadium = 0
            venue_Sawai_Mansingh_Stadium = 0
            venue_Shaheed_Veer_Narayan_Singh_International_Stadium = 0
            venue_Sharjah_Cricket_Stadium = 0
            venue_Sheikh_Zayed_Stadium = 0
            venue_Wankhede_Stadium = 0
        elif venue == 'Feroz Shah Kotla':
            venue_Dr_YS_Rajasekhara_Reddy_ACA_VDCA_Cricket_Stadium = 0
            venue_Dubai_International_Cricket_Stadium = 0
            venue_Eden_Gardens = 0
            venue_Feroz_Shah_Kotla = 1
            venue_Green_Park = 0
            venue_Holkar_Cricket_Stadium = 0
            venue_M_Chinnaswamy_Stadium = 0
            venue_MA_Chidambaram_Stadium_Chepauk = 0
            venue_Maharashtra_Cricket_Association_Stadium = 0
            venue_Punjab_Cricket_Association_IS_Bindra_Stadium_Mohali = 0
            venue_Rajiv_Gandhi_International_Stadium_Uppal = 0
            venue_Saurashtra_Cricket_Association_Stadium = 0
            venue_Sawai_Mansingh_Stadium = 0
            venue_Shaheed_Veer_Narayan_Singh_International_Stadium = 0
            venue_Sharjah_Cricket_Stadium = 0
            venue_Sheikh_Zayed_Stadium = 0
            venue_Wankhede_Stadium = 0
        elif venue == 'Green Park':
            venue_Dr_YS_Rajasekhara_Reddy_ACA_VDCA_Cricket_Stadium = 0
            venue_Dubai_International_Cricket_Stadium = 0
            venue_Eden_Gardens = 0
            venue_Feroz_Shah_Kotla = 0
            venue_Green_Park = 1
            venue_Holkar_Cricket_Stadium = 0
            venue_M_Chinnaswamy_Stadium = 0
            venue_MA_Chidambaram_Stadium_Chepauk = 0
            venue_Maharashtra_Cricket_Association_Stadium = 0
            venue_Punjab_Cricket_Association_IS_Bindra_Stadium_Mohali = 0
            venue_Rajiv_Gandhi_International_Stadium_Uppal = 0
            venue_Saurashtra_Cricket_Association_Stadium = 0
            venue_Sawai_Mansingh_Stadium = 0
            venue_Shaheed_Veer_Narayan_Singh_International_Stadium = 0
            venue_Sharjah_Cricket_Stadium = 0
            venue_Sheikh_Zayed_Stadium = 0
            venue_Wankhede_Stadium = 0
        elif venue == 'Holkar Cricket Stadium':
            venue_Dr_YS_Rajasekhara_Reddy_ACA_VDCA_Cricket_Stadium = 0
            venue_Dubai_International_Cricket_Stadium = 0
            venue_Eden_Gardens = 0
            venue_Feroz_Shah_Kotla = 0
            venue_Green_Park = 0
            venue_Holkar_Cricket_Stadium = 1
            venue_M_Chinnaswamy_Stadium = 0
            venue_M.Chinnaswamy_Stadium = 0
            venue_MA_Chidambaram_Stadium_Chepauk = 0
            venue_Maharashtra_Cricket_Association_Stadium = 0
            venue_Punjab_Cricket_Association_IS_Bindra_Stadium_Mohali = 0
            venue_Rajiv_Gandhi_International_Stadium_Uppal = 0
            venue_Saurashtra_Cricket_Association_Stadium = 0
            venue_Sawai_Mansingh_Stadium = 0
            venue_Shaheed_Veer_Narayan_Singh_International_Stadium = 0
            venue_Sharjah_Cricket_Stadium = 0
            venue_Sheikh_Zayed_Stadium = 0
            venue_Wankhede_Stadium = 0
        elif venue == 'M Chinnaswamy Stadium':
            venue_Dr_YS_Rajasekhara_Reddy_ACA_VDCA_Cricket_Stadium = 0
            venue_Dubai_International_Cricket_Stadium = 0
            venue_Eden_Gardens = 0
            venue_Feroz_Shah_Kotla = 0
            venue_Green_Park = 0
            venue_Holkar_Cricket_Stadium = 0
            venue_M_Chinnaswamy_Stadium = 1
            venue_MA_Chidambaram_Stadium_Chepauk = 0
            venue_Maharashtra_Cricket_Association_Stadium = 0
            venue_Punjab_Cricket_Association_IS_Bindra_Stadium_Mohali = 0
            venue_Rajiv_Gandhi_International_Stadium_Uppal = 0
            venue_Saurashtra_Cricket_Association_Stadium = 0
            venue_Sawai_Mansingh_Stadium = 0
            venue_Shaheed_Veer_Narayan_Singh_International_Stadium = 0
            venue_Sharjah_Cricket_Stadium = 0
            venue_Sheikh_Zayed_Stadium = 0
            venue_Wankhede_Stadium = 0
        elif venue == 'MA Chidambaram Stadium, Chepauk':
            venue_Dr_YS_Rajasekhara_Reddy_ACA_VDCA_Cricket_Stadium = 0
            venue_Dubai_International_Cricket_Stadium = 0
            venue_Eden_Gardens = 0
            venue_Feroz_Shah_Kotla = 0
            venue_Green_Park = 0
            venue_Holkar_Cricket_Stadium = 0
            venue_M_Chinnaswamy_Stadium = 0
            venue_MA_Chidambaram_Stadium_Chepauk = 1
            venue_Maharashtra_Cricket_Association_Stadium = 0
            venue_Punjab_Cricket_Association_IS_Bindra_Stadium_Mohali = 0
            venue_Rajiv_Gandhi_International_Stadium_Uppal = 0
            venue_Saurashtra_Cricket_Association_Stadium = 0
            venue_Sawai_Mansingh_Stadium = 0
            venue_Shaheed_Veer_Narayan_Singh_International_Stadium = 0
            venue_Sharjah_Cricket_Stadium = 0
            venue_Sheikh_Zayed_Stadium = 0
            venue_Wankhede_Stadium = 0
        elif venue == 'Maharashtra Cricket Association Stadium':
            venue_Dr_YS_Rajasekhara_Reddy_ACA_VDCA_Cricket_Stadium = 0
            venue_Dubai_International_Cricket_Stadium = 0
            venue_Eden_Gardens = 0
            venue_Feroz_Shah_Kotla = 0
            venue_Green_Park = 0
            venue_Holkar_Cricket_Stadium = 0
            venue_M_Chinnaswamy_Stadium = 0
            venue_MA_Chidambaram_Stadium_Chepauk = 0
            venue_Maharashtra_Cricket_Association_Stadium = 1
            venue_Punjab_Cricket_Association_IS_Bindra_Stadium_Mohali = 0
            venue_Rajiv_Gandhi_International_Stadium_Uppal = 0
            venue_Saurashtra_Cricket_Association_Stadium = 0
            venue_Sawai_Mansingh_Stadium = 0
            venue_Shaheed_Veer_Narayan_Singh_International_Stadium = 0
            venue_Sharjah_Cricket_Stadium = 0
            venue_Sheikh_Zayed_Stadium = 0
            venue_Wankhede_Stadium = 0
        elif venue == 'Punjab Cricket Association IS Bindra Stadium, Mohali':
            venue_Dr_YS_Rajasekhara_Reddy_ACA_VDCA_Cricket_Stadium = 0
            venue_Dubai_International_Cricket_Stadium = 0
            venue_Eden_Gardens = 0
            venue_Feroz_Shah_Kotla = 0
            venue_Green_Park = 0
            venue_Holkar_Cricket_Stadium = 0
            venue_M_Chinnaswamy_Stadium = 0
            venue_MA_Chidambaram_Stadium_Chepauk = 0
            venue_Maharashtra_Cricket_Association_Stadium = 0
            venue_Punjab_Cricket_Association_IS_Bindra_Stadium_Mohali = 1
            venue_Rajiv_Gandhi_International_Stadium_Uppal = 0
            venue_Saurashtra_Cricket_Association_Stadium = 0
            venue_Sawai_Mansingh_Stadium = 0
            venue_Shaheed_Veer_Narayan_Singh_International_Stadium = 0
            venue_Sharjah_Cricket_Stadium = 0
            venue_Sheikh_Zayed_Stadium = 0
            venue_Wankhede_Stadium = 0
        elif venue == 'Rajiv Gandhi International Stadium, Uppal':
            venue_Dr_YS_Rajasekhara_Reddy_ACA_VDCA_Cricket_Stadium = 0
            venue_Dubai_International_Cricket_Stadium = 0
            venue_Eden_Gardens = 0
            venue_Feroz_Shah_Kotla = 0
            venue_Green_Park = 0
            venue_Holkar_Cricket_Stadium = 0
            venue_M_Chinnaswamy_Stadium = 0
            venue_MA_Chidambaram_Stadium_Chepauk = 0
            venue_Maharashtra_Cricket_Association_Stadium = 0
            venue_Punjab_Cricket_Association_IS_Bindra_Stadium_Mohali = 0
            venue_Rajiv_Gandhi_International_Stadium_Uppal = 1
            venue_Saurashtra_Cricket_Association_Stadium = 0
            venue_Sawai_Mansingh_Stadium = 0
            venue_Shaheed_Veer_Narayan_Singh_International_Stadium = 0
            venue_Sharjah_Cricket_Stadium = 0
            venue_Sheikh_Zayed_Stadium = 0
            venue_Wankhede_Stadium = 0
        elif venue == 'Saurashtra Cricket Association Stadium':
            venue_Dr_YS_Rajasekhara_Reddy_ACA_VDCA_Cricket_Stadium = 0
            venue_Dubai_International_Cricket_Stadium = 0
            venue_Eden_Gardens = 0
            venue_Feroz_Shah_Kotla = 0
            venue_Green_Park = 0
            venue_Holkar_Cricket_Stadium = 0
            venue_M_Chinnaswamy_Stadium = 0
            venue_MA_Chidambaram_Stadium_Chepauk = 0
            venue_Maharashtra_Cricket_Association_Stadium = 0
            venue_Punjab_Cricket_Association_IS_Bindra_Stadium_Mohali = 0
            venue_Rajiv_Gandhi_International_Stadium_Uppal = 0
            venue_Saurashtra_Cricket_Association_Stadium = 1
            venue_Sawai_Mansingh_Stadium = 0
            venue_Shaheed_Veer_Narayan_Singh_International_Stadium = 0
            venue_Sharjah_Cricket_Stadium = 0
            venue_Sheikh_Zayed_Stadium = 0
            venue_Wankhede_Stadium = 0
        elif venue == 'Sawai Mansingh Stadium':
            venue_Dr_YS_Rajasekhara_Reddy_ACA_VDCA_Cricket_Stadium = 0
            venue_Dubai_International_Cricket_Stadium = 0
            venue_Eden_Gardens = 0
            venue_Feroz_Shah_Kotla = 0
            venue_Green_Park = 0
            venue_Holkar_Cricket_Stadium = 0
            venue_M_Chinnaswamy_Stadium = 0
            venue_MA_Chidambaram_Stadium_Chepauk = 0
            venue_Maharashtra_Cricket_Association_Stadium = 0
            venue_Punjab_Cricket_Association_IS_Bindra_Stadium_Mohali = 0
            venue_Rajiv_Gandhi_International_Stadium_Uppal = 0
            venue_Saurashtra_Cricket_Association_Stadium = 0
            venue_Sawai_Mansingh_Stadium = 1
            venue_Shaheed_Veer_Narayan_Singh_International_Stadium = 0
            venue_Sharjah_Cricket_Stadium = 0
            venue_Sheikh_Zayed_Stadium = 0
            venue_Wankhede_Stadium = 0
        elif venue == 'Shaheed Veer Narayan Singh International Stadium':
            venue_Dr_YS_Rajasekhara_Reddy_ACA_VDCA_Cricket_Stadium = 0
            venue_Dubai_International_Cricket_Stadium = 0
            venue_Eden_Gardens = 0
            venue_Feroz_Shah_Kotla = 0
            venue_Green_Park = 0
            venue_Holkar_Cricket_Stadium = 0
            venue_M_Chinnaswamy_Stadium = 0
            venue_MA_Chidambaram_Stadium_Chepauk = 0
            venue_Maharashtra_Cricket_Association_Stadium = 0
            venue_Punjab_Cricket_Association_IS_Bindra_Stadium_Mohali = 0
            venue_Rajiv_Gandhi_International_Stadium_Uppal = 0
            venue_Saurashtra_Cricket_Association_Stadium = 0
            venue_Sawai_Mansingh_Stadium = 0
            venue_Shaheed_Veer_Narayan_Singh_International_Stadium = 1
            venue_Sharjah_Cricket_Stadium = 0
            venue_Sheikh_Zayed_Stadium = 0
            venue_Wankhede_Stadium = 0
        elif venue == 'Sharjah Cricket Stadium':
            venue_Dr_YS_Rajasekhara_Reddy_ACA_VDCA_Cricket_Stadium = 0
            venue_Dubai_International_Cricket_Stadium = 0
            venue_Eden_Gardens = 0
            venue_Feroz_Shah_Kotla = 0
            venue_Green_Park = 0
            venue_Holkar_Cricket_Stadium = 0
            venue_M_Chinnaswamy_Stadium = 0
            venue_MA_Chidambaram_Stadium_Chepauk = 0
            venue_Maharashtra_Cricket_Association_Stadium = 0
            venue_Punjab_Cricket_Association_IS_Bindra_Stadium_Mohali = 0
            venue_Rajiv_Gandhi_International_Stadium_Uppal = 0
            venue_Saurashtra_Cricket_Association_Stadium = 0
            venue_Sawai_Mansingh_Stadium = 0
            venue_Shaheed_Veer_Narayan_Singh_International_Stadium = 0
            venue_Sharjah_Cricket_Stadium = 1
            venue_Sheikh_Zayed_Stadium = 0
            venue_Wankhede_Stadium = 0
        elif venue == 'Sheikh Zayed Stadium':
            venue_Dr_YS_Rajasekhara_Reddy_ACA_VDCA_Cricket_Stadium = 0
            venue_Dubai_International_Cricket_Stadium = 0
            venue_Eden_Gardens = 0
            venue_Feroz_Shah_Kotla = 0
            venue_Green_Park = 0
            venue_Holkar_Cricket_Stadium = 0
            venue_M_Chinnaswamy_Stadium = 0
            venue_MA_Chidambaram_Stadium_Chepauk = 0
            venue_Maharashtra_Cricket_Association_Stadium = 0
            venue_Punjab_Cricket_Association_IS_Bindra_Stadium_Mohali = 0
            venue_Rajiv_Gandhi_International_Stadium_Uppal = 0
            venue_Saurashtra_Cricket_Association_Stadium = 0
            venue_Sawai_Mansingh_Stadium = 0
            venue_Shaheed_Veer_Narayan_Singh_International_Stadium = 0
            venue_Sharjah_Cricket_Stadium = 0
            venue_Sheikh_Zayed_Stadium = 1
            venue_Wankhede_Stadium = 0
        elif venue == 'Wankhede Stadium':
            venue_Dr_YS_Rajasekhara_Reddy_ACA_VDCA_Cricket_Stadium = 0
            venue_Dubai_International_Cricket_Stadium = 0
            venue_Eden_Gardens = 0
            venue_Feroz_Shah_Kotla = 0
            venue_Green_Park = 0
            venue_Holkar_Cricket_Stadium = 0
            venue_M_Chinnaswamy_Stadium = 0
            venue_MA_Chidambaram_Stadium_Chepauk = 0
            venue_Maharashtra_Cricket_Association_Stadium = 0
            venue_Punjab_Cricket_Association_IS_Bindra_Stadium_Mohali = 0
            venue_Rajiv_Gandhi_International_Stadium_Uppal = 0
            venue_Saurashtra_Cricket_Association_Stadium = 0
            venue_Sawai_Mansingh_Stadium = 0
            venue_Shaheed_Veer_Narayan_Singh_International_Stadium = 0
            venue_Sharjah_Cricket_Stadium = 0
            venue_Sheikh_Zayed_Stadium = 0
            venue_Wankhede_Stadium = 1
        
        inning = int(request.form['ae'])
        
        overs = float(request.form['af'])
        over = int(overs / 1)
        ball = np.round((overs % 1) * 10, 0)
        
        runs = int(request.form['ag'])
        
        wickets = int(request.form['ah'])
        
        runs_last_5_overs = int(request.form['ai'])
        
        wickets_last_5_overs = int(request.form['aj'])
        
        entries = [batting_team_Chennai_Super_Kings, batting_team_Delhi_Capitals, batting_team_Gujarat_Lions, batting_team_Kings_XI_Punjab, batting_team_Kolkata_Knight_Riders, batting_team_Mumbai_Indians, batting_team_Rajasthan_Royals, batting_team_Rising_Pune_Supergiant, batting_team_Royal_Challengers_Bangalore, batting_team_Sunrisers_Hyderabad, bowling_team_Chennai_Super_Kings, bowling_team_Delhi_Capitals, bowling_team_Gujarat_Lions, bowling_team_Kings_XI_Punjab, bowling_team_Kolkata_Knight_Riders, bowling_team_Mumbai_Indians, bowling_team_Rajasthan_Royals, bowling_team_Rising_Pune_Supergiant, bowling_team_Royal_Challengers_Bangalore, bowling_team_Sunrisers_Hyderabad, toss_decision_bat, toss_decision_field, venue_Dr_YS_Rajasekhara_Reddy_ACA_VDCA_Cricket_Stadium, venue_Dubai_International_Cricket_Stadium, venue_Eden_Gardens, venue_Feroz_Shah_Kotla, venue_Green_Park, venue_Holkar_Cricket_Stadium, venue_M_Chinnaswamy_Stadium, venue_MA_Chidambaram_Stadium_Chepauk, venue_Maharashtra_Cricket_Association_Stadium, venue_Punjab_Cricket_Association_IS_Bindra_Stadium_Mohali, venue_Rajiv_Gandhi_International_Stadium_Uppal, venue_Saurashtra_Cricket_Association_Stadium, venue_Sawai_Mansingh_Stadium, venue_Shaheed_Veer_Narayan_Singh_International_Stadium, venue_Sharjah_Cricket_Stadium, venue_Sheikh_Zayed_Stadium, venue_Wankhede_Stadium, inning, over, ball, runs, wickets, runs_last_5_overs, wickets_last_5_overs]
        entries = np.array([entries])
        entries = entries.reshape(1, -1)
        
        prediction = model.predict(entries)[0]
        low = prediction - (0.12 * prediction)
        low = int(np.round(low, 0))
        high = prediction + (0.12 * prediction)
        high = int(np.round(high, 0))

        if low < runs:
            if runs < high:
                return render_template('predict.html', prediction_text = '{} would be scoring most probably inbetween {} - {}'.format(batting_team, runs, high))
            else:
                return render_template('predict.html', prediction_text = '{} would be scoring most probably inbetween {} - {}'.format(batting_team, low, high))
            
        else:
            return render_template('predict.html', prediction_text = '{} would be scoring most probably inbetween {} - {}'.format(batting_team, low, high))    
    else:
        return render_template('home.html')
if __name__=="__main__":
    #app.run(host = '0.0.0.0', port = 8080)
    #app.run(debug = True)
    app.run()
