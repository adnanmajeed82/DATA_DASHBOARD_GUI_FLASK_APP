from flask import Flask, render_template
import plotly.express as px
import pandas as pd

app = Flask(__name__)

# Mock data
data = {
    'Category': ['Karachi', 'Lahore', 'Islamabad', 'Peshawar', 'Quetta'],
    'Value': [22, 10, 9, 11, 14]
}

df = pd.DataFrame(data)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    # Plotting the bar chart
    fig = px.bar(df, x='Category', y='Value', title='Data Dashboard')

    # You can customize the chart here (e.g., add labels, change colors, etc.)

    # Save the chart to HTML
    chart_html = fig.to_html(full_html=False)

    return render_template('dashboard.html', chart_html=chart_html)


if __name__ == '__main__':
    app.run(debug=True)
