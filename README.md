# ABM-Ldgr.py

The <b>ABM-Ldgr.py</b> toolkit supports flow of funds agent-based models with a shared ledger framework. The project began while building our second financial system agent-based model. The first model investigated the dynamics of the US corporate bond market (see <a href="https://doi.org/10.3390/systems5040054">doi.org/10.3390/systems5040054</a>). The second model focused on the US Federal Reserve, along with the banking sector that maintains reserve accounts using a flow-of-funds perspective. One way the Fed can implement monetary policy is through <i>quantitative easing</i> (QE) or <i>quantitative tightening</i> (QT) policies. A QE strategy entails large-scale asset purchases, increasing the money supply, which helps lower interest rates. The lower cost of borrowing then fosters economic growth. QT reverses the process, shrinking the Fed balance sheet and tightening the economic conditions.

While implementing the Fed flow-of-funds model, each autonomous agent encapsulates a set of financial accounts (like organizations in the real world).  However, these decentralized accounts are logically related through a series of transactions and needed to be reconciled to ensure the stability of the money supply. The idea of sharing accounts across agent (or organizational) boundaries promised to simplify the code base.  There was not much need for a true distributed ledger as implemented by blockchain technologies, at least for now. Agents could simply share the same account objects, thereby creating financial connections. For a description of the first Fed model, see <a href="https://dl.acm.org/doi/10.5555/3374138.3374167">dl.acm.org/doi/10.5555/3374138.3374167</a>. This early flow-of-funds use case demonstrated the advantages of using a shared ledger-like functionality for such models, hence the <b>ABM-Ldgr.py</b> toolkit. The second version of the Fed agent-based model was much simpler and easier to maintain, with a richer set of reporting capabilities.

The <b>Account</b> class provides the basic functionality, including methods to deposit and withdraw funds, as well as check the current balance. Accounts can be grouped into using the <b>Ledger</b> class. For example, all the accounts that represent assets be grouped. The assets ledger can be paired with a liabilities ledger using the <b>BalanceSheet</b> class as part of the internal agent financial data. Again, the instantiated accounts and ledgers can be shared across two or more agents to make financial connections, implementing "flow-of-funds" models.

# Availability

A prototype versions is available on Test PyPI at <a href="https://test.pypi.org/project/usf-ledger-package">test.pypi.org/project/usf-ledger-package</a>.

A single file is available here in the repository for use in any Python project.  Simply download the <b>abm-ldgr.py</b> file and import as "from abm-ldgr import *" to use the clases to instantiate accounts, group them as ledgers and create balance sheets.

The <b>ABM-Ldgr.py</b> toolkit is in use on several on-going projects.  New features and refinements are underway for future versions.

# Acknowledgements

Coordinator: Don Berndt (<a href="mailto:dberndt@usf.edu">dberndt@usf.edu</a>)

Contributors (Committers): David Boogers, Sonal Prabhune (C), Daniel Lasa

