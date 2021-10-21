import sys
import os
import re

invoice = {
    'in_number': '',
    'in_date': '',
    'bill_info': '',
    'ship_info': '',
    'email': '',
    'product_description': '',
    'product_name': '',
    'product_qty':'',
    'product_price':'',
    'product_tax':'',
    'product_subtotal':'',
    'product_ship': '',
    'product_total': '',
    'product_note': ''
}

def find_following_line(file, pattern, slise):
    lines = []
    
    with open(file) as f:
        for line in f:
            line = line.rstrip()
            lines.append(line)
            
        for i, line in enumerate(lines):
            if re.search(pattern, line):
                return lines[i + slise[0]:i + slise[1]]
    
def setItem(pattern, string, key):
    result = re.search(pattern, string)
    if result:
        invoice[key] = result.group(1)


def main():
    if len(sys.argv) != 3:
        print('Use <script name> <input file> <oupput file>, please')
        sys.exit(1)
    
    fileIn = sys.argv[1]
    fileOut = sys.argv[2]
    
    if not os.path.isfile(fileIn):
        print('error: {} does not exist'.format(fileIn))
        sys.exit(1)
        
    if os.path.isfile(fileOut):
        print('{} exists. Override (y/n)?'.format(fileOut))
        reply = input().strip().lower()
        if reply[0] != 'y':
            sys.exit(1)
            
    lines = []
    
    lines = find_following_line(fileIn, "Billing Information Shipping Information",(1,5))
    invoice['bill_info'] = lines[0:2]
    invoice['ship_info'] = lines[2:4]
    
    lines = find_following_line(fileIn, "Price",(1,3))
    
    invoice['product_description'] = lines[0:1]
    
    unit = ''.join(lines[1:2])
    
    setItem("\$(\d+\.\d+)", unit, 'product_price')
    setItem("(\d+)", unit, 'product_qty')
    setItem("([a-zA-Z :_.-]+)", unit, 'product_name')
    
    with open(fileIn, 'r') as f:
        for line in f:
            line = line.rstrip()
            setItem("INV-([0-9]+)", line, 'in_number')
            setItem("Subtotal \$(\d+\.\d+)", line, 'product_subtotal')
            setItem("Shipping \$(\d+\.\d+)", line, 'product_ship')
            setItem("([0-9]+\/[0-9]+\/[0-9]{4})", line, 'in_date')
            setItem("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+)", line, 'email')
            
    with open(fileOut, 'w') as f:
        f.write(f"{invoice}\n")

if __name__ == '__main__':
    main()
    