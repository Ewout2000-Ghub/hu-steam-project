def merge_sort(arr, filter_key):
    if len(arr) > 1: # Als de lijst langer is dan 1

        # Het midden van de lijst
        midden = len(arr) // 2

        # Linkerkant van de lijst
        links = arr[:midden]

        # Rechterkant van de lijst
        rechts = arr[midden:]

        # Sorteer de linkerkant
        merge_sort(links, filter_key)

        # Sorteer de rechterkant
        merge_sort(rechts, filter_key)

        index_links = 0
        index_rechts = 0
        key = 0

        # Zo lang als de index_links en index_rechts beide kleiner zijn dan de lijsten
        while index_links < len(links) and index_rechts < len(rechts):
            # Check of de key links kleiner is dan de key rechts
            if links[index_links][filter_key] < rechts[index_rechts][filter_key]:
                arr[key] = links[index_links]
                index_links += 1
            else:
                arr[key] = rechts[index_rechts]
                index_rechts += 1
            key += 1

        # Zo lang als de index_links kleiner is dan de lijst
        while index_links < len(links):
            arr[key] = links[index_links]
            index_links += 1
            key += 1

        # Zo lang als de index_rechts kleiner is dan de lijst
        while index_rechts < len(rechts):
            arr[key] = rechts[index_rechts]
            index_rechts += 1
            key += 1