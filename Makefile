run:
	python run_all.py

dashboard:
	streamlit run dashboard/pipeline_dashboard.py

install:
	pip install -r requirements.txt

clean:
	rm -rf outputs
	rm -rf logs