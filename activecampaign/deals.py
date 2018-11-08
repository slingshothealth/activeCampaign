class Deals(object):

    def __init__(self, client):
        self.client = client

    def get_stage_list(self):
        return self.client._get('deal_stage_list')

    def get_stage_id(self, stage):

        stage_list = self.get_stage_list()

        for key, val in stage_list.items():
            if type(val) is dict and val['title'] == stage:
                return val['id']


    '''
        Available Fields to Create a Deal
        title*          Title of the new deal. Example: 'Deal Title'
        value*          Value of the new deal in dollars. Example: '450.00' or 450
        currency*       Currency of the new deal. Example: 'usd'
        pipeline*       ID of the new deal's pipeline. Example: '3' (Get available pipeline IDs with "deal_pipeline_list" call)
        stage*          ID of the new deal's stage. Example: '52' (Get available stage IDs with "deal_stage_list" call)
        contactid       ID of an existing contact for the new deal. Example: '8'. NOTE: IF THIS IS NOT PROVIDED, 'contact' MUST BE. (Get available contact IDs with "contact_list" call)
        contact_name    Name of the contact for the new deal. Example: 'John Doe'
        organization    Name of the organization of the contact for the new deal. Example: 'Acme Corp'
    '''

    def add(self, title, value, pipeline, stage, contact_id):

        stage_id = self.get_stage_id(stage)

        additional_data = [
            ('title', title),
            ('value', value),
            ('currency', 'usd'),
            ('pipeline', pipeline),
            ('stage', stage_id),
            ('contactid', contact_id),
        ]
        return self.client._post('deal_add', additional_data)

    '''
        Available Fields to edit a Deal
        id*              ID of the deal to update. Example: '2' (Get available deal IDs with "deal_list" call)
        currency        Currency of the new deal. Example: 'usd'
        pipeline        ID of the new deal's pipeline. Example: '3' (Get available pipeline IDs with "deal_pipeline_list" call)
        userid          ID of the user who owns the deal. Example: '14' (Get available owner IDs with "user_list" call)
        status          Status of the deal. Options: '0' (open), '1' (won), '2' (lost)
    '''

    def edit(self, id, stage, status, value = None):

        stage_id = self.get_stage_id(stage)

        additional_data = [
            ('id', id),
            ('stage', stage_id),
            ('status', status)
        ]

        if value:
            additional_data.append('value', value)

        return self.client._post('deal_edit', additional_data)

    '''
        Available Fields to add a note to a deal
        note*       Text of the note. Example: 'Follow up about this deal soon'
        dealid*     ID of the deal for the new deal note. Example: '31' (Get available deal IDs with "deal_list" call)
        owner       ID of the owner of the new deal note. Example: '4' (Get available owner IDs with "user_list" call)
    '''

    def add_note(self, note, deal_id):
        additional_data = [
            ('note', note),
            ('dealid', deal_id),
        ]
        return self.client._post('deal_note_add', additional_data)
