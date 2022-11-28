
from flask_appbuilder import ModelView ,DirectByChartView
from flask_appbuilder.models.sqla.interface import SQLAInterface

from . import appbuilder, db
from .models import Cislo


class CisloView(ModelView):
    datamodel = SQLAInterface(Cislo)

    list_columns = ["cislo"]
    """show_template = "appbuilder/general/model/show_cascade.html"""

class CountryDirectChartView(DirectByChartView):
    datamodel = SQLAInterface(Cislo)
    chart_title = 'graf'

    definitions = [
    {
        'label': 'Cislo',
        'group': 'id',
        'series': ['cislo']

    }
]
db.create_all()

appbuilder.add_view(
    CisloView, "Osoby", icon="fa-folder-open-o"
)
appbuilder.add_view(CountryDirectChartView, "Show Country Chart", icon="fa-dashboard", category="Statistics")