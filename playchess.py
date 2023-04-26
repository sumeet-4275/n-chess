from flask import Flask, redirect, url_for, request, render_template
from svglib.svglib import svg2rlg
import driver as dr
import board_functions as bf

app = Flask(__name__)

@app.route('/')
def home():
    #boardgui = svg2rlg('board.svg')
    return render_template('base.html')

@app.route('/pvp')
def pvp():
    svgboard = dr.player_vs_player(bf.make_board())
    return render_template('pvp.html', content = svgboard)

@app.route('/pvc')
def pvc():
    svgboard = dr.player_vs_computer(dr.board)
    return render_template('pvp.html', content = svgboard)

@app.route('/cvc')
def cvc():
    svgboard = dr.computer_vs_computer(dr.board)
    return render_template('pvp.html', content = svgboard)

if __name__ == '__main__':
    app.run(debug=True)