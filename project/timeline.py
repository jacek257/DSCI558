from scrapy import Selector

def parse_timeline(response):

    for target in response.css('div.bkbqAE').getall():

        z = Selector(text=target)

        mins_raw = z.css('p.kIsgYX::text').getall()
        mins_parsed = [mins_raw[i] + mins_raw[i+1] for i in range(0,len(mins_raw),2)]
        # print(mins_parsed)
        actions = z.css('div::text').getall()
        modifiers = z.css('span::text').getall()

        if len(mins_parsed) == 0 or len(actions) == 0 or len(modifiers) == 0:
            continue

        actions_reorgnized = []

        try:
            i, j = 0, 0
            for min in mins_parsed:
                # Assign current action
                action = actions[i]
                if action.startswith('You destroyed') or action.startswith('Assisted with destroying'):
                    actions_reorgnized.append( (min, action + modifiers[j]) )
                    i += 1
                    j += 1
                elif action.startswith('Placed'): # Placed a ward
                    actions_reorgnized.append( (min, action) )
                    i += 1
                elif action.startswith('You') or action.startswith('Assist'): # kill
                    actions_reorgnized.append( (min, action + modifiers[j] + actions[i+1] ) )
                    i += 2
                    j += 1
                elif modifiers[j].strip() == 'killed': # gets killed
                    actions_reorgnized.append( (min, action + modifiers[j] + actions[i+1]) )
                    i += 2
                    j += 1

            return actions_reorgnized
        except:
            return [mins_parsed, actions, modifiers]
