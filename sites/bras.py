#
#
#
# bras > https://bras.ro/cariere-bras/

from sites.website_scraper_bs4 import BS4Scraper

class brasScraper(BS4Scraper):
    
    """
    A class for scraping job data from bras website.
    """
    url = 'https://bras.ro/cariere-bras/'
    url_logo = 'https://bras.ro/wp-content/uploads/bras-negru-5.png'
    company_name = 'bras'
    
    
    def __init__(self):
        """
        Initialize the BS4Scraper class.
        """
        self.job_count = 1
        super().__init__(self.company_name, self.url_logo)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from bras website.
        """

        job_elements = self.get_jobs_elements('class_', 'pagelayer-accordion-tabs')
        
        self.job_titles = self.get_jobs_details_text(job_elements)

        self.format_data()
        
    def sent_to_future(self):
        self.send_to_viitor()
    
    def return_data(self):
        self.get_response()
        self.scrape_jobs()
        return self.formatted_data, self.company_name

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title in self.job_titles:
            job_url = self.url + "#" + str(self.job_count)
            self.create_jobs_dict(job_title, job_url, "România", "Iasi")
            self.job_count += 1

if __name__ == "__main__":
    bras = brasScraper()
    bras.get_response()
    bras.scrape_jobs()
    bras.sent_to_future()
    
    

