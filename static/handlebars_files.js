(function() {
  var template = Handlebars.template, templates = Handlebars.templates = Handlebars.templates || {};
templates['handlebars_files.hbs'] = template(function (Handlebars,depth0,helpers,partials,data) {
  this.compilerInfo = [2,'>= 1.0.0-rc.3'];
helpers = helpers || Handlebars.helpers; data = data || {};
  var buffer = "", stack1, functionType="function", escapeExpression=this.escapeExpression, self=this;

function program1(depth0,data) {
  
  var buffer = "", stack1, stack2;
  buffer += "\n  <label><input type='radio' class='radio-button' name='address' data-address='"
    + escapeExpression(((stack1 = ((stack1 = depth0.location),stack1 == null || stack1 === false ? stack1 : stack1.address)),typeof stack1 === functionType ? stack1.apply(depth0) : stack1))
    + " "
    + escapeExpression(((stack1 = ((stack1 = depth0.location),stack1 == null || stack1 === false ? stack1 : stack1.crossStreet)),typeof stack1 === functionType ? stack1.apply(depth0) : stack1))
    + "' data-name='";
  if (stack2 = helpers.name) { stack2 = stack2.call(depth0, {hash:{},data:data}); }
  else { stack2 = depth0.name; stack2 = typeof stack2 === functionType ? stack2.apply(depth0) : stack2; }
  buffer += escapeExpression(stack2)
    + "'><b>";
  if (stack2 = helpers.name) { stack2 = stack2.call(depth0, {hash:{},data:data}); }
  else { stack2 = depth0.name; stack2 = typeof stack2 === functionType ? stack2.apply(depth0) : stack2; }
  buffer += escapeExpression(stack2)
    + "</b>: "
    + escapeExpression(((stack1 = ((stack1 = depth0.location),stack1 == null || stack1 === false ? stack1 : stack1.address)),typeof stack1 === functionType ? stack1.apply(depth0) : stack1))
    + " "
    + escapeExpression(((stack1 = ((stack1 = depth0.location),stack1 == null || stack1 === false ? stack1 : stack1.crossStreet)),typeof stack1 === functionType ? stack1.apply(depth0) : stack1))
    + "</input></label><br />\n  ";
  return buffer;
  }

  buffer += "<div class=\"restaurant-list\"><h3>Addresses</h3>\n  ";
  stack1 = helpers.each.call(depth0, depth0.venues, {hash:{},inverse:self.noop,fn:self.program(1, program1, data),data:data});
  if(stack1 || stack1 === 0) { buffer += stack1; }
  buffer += "\n</div>\n";
  return buffer;
  });
})();