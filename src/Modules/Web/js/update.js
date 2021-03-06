/**
 * @name:      PyHouse/src/Modules/Web/js/8pdate.js
 * @author:    D. Brian Kimmel
 * @contact:   D.BrianKimmel@gmail.com
 * @copyright: (c) 2015 by D. Brian Kimmel
 * @license:   MIT License
 * @note:      Created on June 18, 2015
 * @summary:   Displays the update element
 *
 */

helpers.Widget.subclass(update, 'UpdateWidget').methods(

	function __init__(self, node) {
		update.UpdateWidget.upcall(self, '__init__', node);
	},



// ============================================================================
	/**
     * Place the widget in the workspace.
	 * 
	 * @param self is    <"Instance" of undefined.update.UpdateWidget>
	 * @returns a deferred
	 */
	function ready(self) {
		function cb_widgetready(res) {
			self.hideWidget();
		}
		var uris = collectIMG_src(self.node, null);
		var l_defer = loadImages(uris);
		l_defer.addCallback(cb_widgetready);
		return l_defer;
	},
	/**
	 * Show the update widget
	 */
	function startWidget(self) {
		self.node.style.display = 'block';
		showSelectionButtons(self);
		self.fetchDataFromServer();
	},



// ============================================================================
	/**
	 * This triggers getting the data from the server.
	 */
	function fetchDataFromServer(self) {
		function cb_fetchDataFromServer(p_json) {
			globals.Computer = JSON.parse(p_json);
			self.buildLcarSelectScreen();
		}
		function eb_fetchDataFromServer(p_result) {
			Divmod.debug('---', 'update.eb_fetchDataFromServer() was called. ERROR = ' + p_result);
		}
        var l_defer = self.callRemote("getServerData");  // @ web_update.py
		l_defer.addCallback(cb_fetchDataFromServer);
		l_defer.addErrback(eb_fetchDataFromServer);
        return false;
	},
	/**
	 * Build a screen full of buttons - One for each item and some actions.
	 */
	function buildLcarSelectScreen(self){
		var l_button_html = buildLcarSelectionButtonsTable(globals.Computer.Update, 'handleMenuOnClick');
		var l_html = build_lcars_top('Update', 'lcars-salmon-color');
		l_html += build_lcars_middle_menu(15, l_button_html);
		l_html += build_lcars_bottom();
		self.nodeById('SelectionButtonsDiv').innerHTML = l_html;
	},
	/**
	 * Event handler for selection buttons.
	 *
	 * The user can click on a selection button or the "Back" button.
	 *
	 * @param self is    <"Instance" of undefined.update.UpdateWidget>
	 * @param p_version is  the node of the button that was clicked.
	 */
	function handleMenuOnClick(self, p_version) {
		var l_ix = p_version.name;
		var l_name = p_version.value;
		globals.Computer.VersionIx = l_ix;
		globals.Computer.VersionName = l_name;
		if (l_ix <= 1000) {  // One of the update buttons.
			var l_obj = globals.Computer.Version[l_ix];
			globals.Computer.VersionObj = l_obj;
			showDataEntryScreen(self);
			self.buildLcarDataEntryScreen(l_obj, 'handleDataEntryOnClick');
		} else if (l_ix == 10002) {  // The "Back" button
			self.showWidget('HouseMenu');
		}
	},


// ============================================================================
	/**
	 * Build a screen full of data entry fields.
	 */
	function buildLcarDataEntryScreen(self, p_entry, p_handler){
		var l_obj = arguments[1];
		var l_html = build_lcars_top('Version Data', 'lcars-salmon-color');
		l_html += build_lcars_middle_menu(20, self.buildEntry(l_obj, p_handler));
		l_html += build_lcars_bottom();
		self.nodeById('DataEntryDiv').innerHTML = l_html;
	},
	function buildEntry(self, p_obj, p_handler, p_onchange) {
		var l_html = buildBaseEntry(self, p_obj);
		l_html = self.buildNodeEntry(p_obj, l_html);
		l_html += buildLcarEntryButtons(p_handler);
		return l_html;
	},
    function buildNodeEntry(self, p_obj, p_html) {
		// p_html += buildLcarTextWidget(self, 'Comment', 'Comment', p_obj.Comment);
		p_html += buildLcarTextWidget(self, 'Addr', 'Broker Address', p_obj.BrokerAddress);
		p_html += buildLcarTextWidget(self, 'Port', 'Port', p_obj.BrokerPort);
		// p_html += buildLcarTextWidget(self, 'Role', 'Node Role', p_obj.NodeRole);
        return p_html;
    },
	function fetchEntry(self) {
    	var l_data = fetchBaseEntry(self);
		l_data = self.fetchNodeEntry(l_data);
        return l_data;
	},
    function fetchNodeEntry(self, p_data) {
        // p_data.Comment = fetchTextWidget(self, 'Comment');
        p_data.BrokerAddress = fetchTextWidget(self, 'Addr');
        p_data.BrokerPort = fetchTextWidget(self, 'Port');
        // p_data.NodeRole = fetchTextWidget(self, 'Role');
    	return p_data;
    },
    function createEntry(self) {
        var l_data = createBaseEntry(self, Object.keys(globals.Computer.Nodes).length);
        l_data = self.createNodeEntry(l_data);
        return l_data;
    },
    function createNodeEntry(self, p_data) {
		// p_data.Comment = '';
		p_data.BrokerAddress = '';
		p_data.BrokerPort = '';
		// p_data.NodeRoll = 0;
        return p_data;
    },


// ============================================================================
	/**
	 * Event handler for update buttons at bottom of entry portion of this widget.
	 * Get the possibly changed data and send it to the server.
	 * 
	 * @param self is   <"Instance" of undefined.update.updateWidget>
	 * @param p_node is the button node that was clicked on
	 */
	function handleDataEntryOnClick(self, p_node) {
		function cb_handleDataEntryOnClick(p_json) {
			self.startWidget();
		}
		function eb_handleDataEntryOnClick(p_reason){
			Divmod.debug('---', 'update.eb_handleDataEntryOnClick() was called. ERROR =' + p_reason);
		}
		var l_ix = p_node.name;
		var l_defer;
		var l_json;
		switch(l_ix) {
		case '10003':  // Change Button
	    	l_json = JSON.stringify(self.fetchEntry());
	        l_defer = self.callRemote("saveUpdateData", l_json);  // @ web_update
			l_defer.addCallback(cb_handleDataEntryOnClick);
			l_defer.addErrback(eb_handleDataEntryOnClick);
			break;
		case '10002':  // Back button
			showSelectionButtons(self);
			break;
		case '10004':  // Delete button
			var l_obj = self.fetchEntry();
			l_obj.Delete = true;
	    	l_json = JSON.stringify(l_obj);
	        l_defer = self.callRemote("saveupdateData", l_json);  // @ web_rooms
			l_defer.addCallback(cb_handleDataEntryOnClick);
			l_defer.addErrback(eb_handleDataEntryOnClick);
			break;
		default:
			Divmod.debug('---', 'update.handleDataEntryOnClick(Default) was called. l_ix:' + l_ix);
			break;
		}
		// return false stops the resetting of the server.
        return false;
	}
);
// Divmod.debug('---', 'update.handleMenuOnClick(1) was called. ' + l_ix + ' ' + l_name);
// console.log("update.handleMenuOnClick() - l_obj = %O", l_obj);
// ### END DBK
