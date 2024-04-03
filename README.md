
# Real-Time BI Dashboard with Streamlit

This project is a real-time Business Intelligence (BI) dashboard built with Streamlit, designed to visualize sales data interactively. The application allows users to filter data based on regions and displays various metrics such as Sales, Expenses, Profit, and Units Sold over time using line and bar charts.

## Features

- **Dynamic Data Filtering**: Users can filter the dataset based on regions using a dropdown menu in the sidebar.
- **Interactive Charts**: The dashboard displays interactive charts for sales, expenses, profit, and units sold over time, enabling users to gain insights at a glance.
- **Real-Time Data Exploration**: Powered by Streamlit, the dashboard updates in real-time as users adjust the filters, providing an interactive data exploration experience.

## Getting Started

### Prerequisites

Ensure you have the following installed:
- Python 3.6 or later
- pip

### Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/KeenSightStreamLit/Real-Time-BI-Dashboard.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Real-Time-BI-Dashboard
   ```

3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

To run the dashboard, execute the following command in the terminal from the project directory:

```bash
streamlit run app.py
```

After running the command, Streamlit will start the application and provide a local URL. Open the URL in a web browser to view the dashboard.

## Data

The dashboard visualizes data loaded from a JSON file (`data.json`). The JSON file should contain records with the following fields: `Date`, `Region`, `Sales`, `Expenses`, `Profit`, and `Units Sold`.

## Development

To add new features or charts to the dashboard, modify the `app.py` script. You can add additional filters, metrics, or visualizations as needed to enhance the dashboard's capabilities.

## License

This project is open-sourced under the MIT License. See the LICENSE file for more details.
