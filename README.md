**Stock Data Parser **

A Python-based utility designed to extract, clean, and normalize financial trading data from unstructured log strings. 

**Overview**
Financial log data is often messy and inconsistent. This project demonstrates a custom-built **Parser** that identifies key data points (Ticker Symbols and Prices) within complex strings, regardless of their length or case sensitivity.



**Key Features**
* **Dynamic Tag Searching:** Uses anchor-based logic (`PRICE:`, `-STATUS`) to locate data without relying on hardcoded indices.
* **Case Insensitivity:** Automatically normalizes log data to handle mixed-case inputs (e.g., `ticker` vs `TICKER`).
* **Symbol Extraction:** Sophisticated slicing logic to extract variable-length ticker symbols (e.g., 3-letter BTC vs 4-letter AAPL).
* **Data Formatting:** Converts raw string fragments into `float` objects with 2-decimal place precision for professional reporting.

**The Parsing Logic:**
1. **Ticker Identification:** The script searches for the `TICKER` label. It calculates the `ticker_lower` limit (start of the symbol) and searches for the next `-PRICE` tag to set the `ticker_upper` limit.
2. **Dynamic Search Window:** To optimize the search for price, the script updates the search starting point (`loc`) to skip over the already-processed ticker data.
3. **Price Extraction:** * It identifies `find_price_start_loc` (PRICE:) and `find_price_end_loc` (-STATUS).
   * It "slices" the string between these two boundaries to isolate the numerical value.
4. **Data Normalization:** The extracted string is cast to a `float` and formatted to 2 decimal places using f-string rounding (`{price:.2f}`).



**Example**
**Raw Input:**
`"ACTION:BUY-TICKER:AAPL-PRICE:150.2587-STATUS:SUCCESS"`

**Parsed Output:**
```text
Ticker found: AAPL
Price of AAPL is 150.26

PS this is my first project
